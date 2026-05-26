from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
from sqlalchemy import create_engine, Integer, String, Float
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, sessionmaker
import time
import os
import logging


db_file_name = "Data/books_data.db"
if os.path.exists(db_file_name):
    os.remove(db_file_name)
    print("Database is deleted")

engine = create_engine("sqlite:///books_data.db")

logging.basicConfig(filename="scraper.log", level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

class Base(DeclarativeBase):
    pass

class Books(Base):
    __tablename__ = "Books"
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    title : Mapped[str] = mapped_column(String, unique=True)
    price : Mapped[float] = mapped_column(Float, nullable=False)
    rating : Mapped[int] = mapped_column(Integer, nullable=False)
    availability : Mapped[str] = mapped_column(String, nullable=False)
    description : Mapped[str] = mapped_column(String)
    url : Mapped[str] = mapped_column(String, nullable=False)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

number_of_pages_completed = 1
total = 3
while number_of_pages_completed  <= total:
    books_to_insert = []

    url = f"https://books.toscrape.com/catalogue/page-{number_of_pages_completed}.html"
    data = requests.get(url=url).text
    soup = BeautifulSoup(data, "html.parser")
    books = soup.find_all(name="article", class_='product_pod')

    for k in books:
        image_url = k.find(name='div', class_='image_container')
        referance_link = image_url.a.get("href")
        full_url = urljoin(url, referance_link)
        h_tag = k.h3
        anchor = h_tag.find("a")
        title = anchor['title']
        des = requests.get(url=full_url).text
        sub_soup = BeautifulSoup(des, "html.parser")
        price = sub_soup.find(name='p', class_="price_color").text.strip().split("£")[-1]
        availability = sub_soup.find(name='p', class_='instock availability').text.strip()
        rat = sub_soup.find(name='div', class_="col-sm-6 product_main")
        book_rating = rat.find_all(name='p')[2]['class'][-1]
        if book_rating.lower() == "one":
            rating = 1
        elif book_rating.lower()=='two':
            rating = 2
        elif book_rating.lower() == 'three':
            rating = 3
        elif book_rating.lower() == 'four':
            rating = 4
        else:
            rating = 5
        des = sub_soup.find(name="div", id='product_description')
        try:
            description = des.find_next_sibling("p").text.strip()
        except:
            logging.warning(f"For the above book there is no description the title of the book is {title} and the page number of the website is {number_of_pages_completed}")
            description = "No Description for the above Book"
        try:
            Book = Books(
                title=title,
                price=float(price),
                rating=int(rating),
                description=description,
                url=full_url,
                availability=availability
            )
        except:
            logging.warning("Some error occured")
            session.rollback()

        books_to_insert.append(Book)
    try:
        session.add_all(books_to_insert)
        session.commit()
        logging.info("One page is added into the database")
    except IntegrityError as e:
        logging.error("The title is repeated twice")
        session.rollback()

    time.sleep(1)
    if number_of_pages_completed==1:
        number_of_pages = soup.find(name='li', class_='current').text.split()[-1]
        total = int(number_of_pages)
        logging.info("We found out the number of pages we should run our loops ")
    number_of_pages_completed +=1