import requests
from sqlalchemy.orm import Session
from models import Country
from logger import logger

def fetch_and_store_countries(db: Session):
    query = """
    query {
        countries {
            code
            name
        }
    }
    """
    try:
        response = requests.post("https://countries.trevorblades.com/", json={"query": query})
        response.raise_for_status()
        countries = response.json()["data"]["countries"]
        logger.info(f"Fetched {len(countries)} countries from GraphQL API")

        for country in countries:
            if not db.query(Country).filter(Country.code == country["code"]).first():
                db_country = Country(name=country["name"], code=country["code"])
                db.add(db_country)
        db.commit()
        logger.info("Countries saved to database")
    except Exception as e:
        logger.error(f"Error fetching or saving countries: {e}")
