import requests
from sqlalchemy.orm import Session
from models import User
from logger import logger

def fetch_and_store_users(db: Session):
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        response.raise_for_status()
        users = response.json()
        logger.info(f"Fetched {len(users)} users from API")

        for user in users:
            if not db.query(User).filter(User.email == user["email"]).first():
                name_parts = user["name"].split(" ", 1)
                first_name = name_parts[0]
                last_name = name_parts[1] if len(name_parts) > 1 else ""
                db_user = User(
                    first_name=first_name,
                    last_name=last_name,
                    email=user["email"],
                    gender="Not Specified",
                    domain="Unknown",
                    available="Yes"
                )
                db.add(db_user)
        db.commit()
        logger.info("Users saved to database")
    except Exception as e:
        logger.error(f"Error fetching or saving users: {e}")
