import aiohttp
from data.sample_mandrill import mandrill_data
import json
from random import randint
from datetime import datetime

from sqlalchemy.orm import Session
from api_dataclasses import MandrillData
from models import MandrillResponse


async def get_api_data():
    data = None

    try:
        """The mandril URL goes here. Activate async block below if Authenticated API from Mandrill is available"""
        # async with aiohttp.ClientSession as session:
        #   data = await session.get('#mandrill_api_url_here', ssl=False)
        #   return data

        """ 
    Data generation to mimic live responses from Mandrill

    1. Importing the sample response data in json format - 'sample_mandrill.py'
    2. Randomizing the response selection sequence to mimic the live API
    """

        response = json.loads(mandrill_data)
        random_integer = randint(0, 9)
        data = response[random_integer]
        return data
        # Note: Deactivate the block above if Authenticated API from Mandrill is available.
    except:
        return f"Something went wrong."


def process_data(data):
    try:
        if data:
            message = data["msg"]
            """create a dictionary to unify data from the response by key-value combination with simpler db-focused references"""
            response_details = {}

            response_details = {
                "event": data["event"],
                "event_id": data["_id"],
                "ts": str(datetime.fromtimestamp(data["ts"])),
                "message_ts": str(datetime.fromtimestamp([message][0]["ts"])),
                "subject": message["subject"],
                "email": message["email"],
                "sender": message["sender"],
                "tags": message["tags"],
                "state": message["state"],
                "message_id": message["_id"],
            }

            """
      - For data streams with no click time, open time, or url data, create dictionary keys with an empty list to create 
        consistency in data saved to database and prevent potential errors. 
      - Populate the keys with relevant data reflecting empty inputs. 
      """

            response_details["time_opened"] = (
                str(datetime.fromtimestamp(message["opens"][0]["ts"]))
                if message.get("opens", [])
                else "Not Opened"
            )
            response_details["time_clicked"] = (
                str(datetime.fromtimestamp(message["clicks"][0]["ts"]))
                if message.get("clicks", [])
                else "-"
            )
            response_details["url_clicked"] = (
                message["clicks"][0]["url"] if message.get("clicks", []) else "No URL"
            )

            return response_details
    except:
        return f"Something went wrong."


def get_all_records(db: Session):
    """Fetch all records from db"""
    try:
        return db.query(MandrillResponse).all()
    except:
        return f"Something went wrong."


def get_record_by_message_id(message_id: str, db: Session):
    """Fetch a single data from db by the message_id"""
    try:
        return (
            db.query(MandrillResponse)
            .filter(MandrillResponse.message_id == message_id)
            .first()
        )
    except:
        return f"Something went wrong."


def create_db_record(mandrill_data: MandrillData, db: Session):
    try:
        db_obj = MandrillResponse(
            event=mandrill_data["event"],
            event_id=mandrill_data["event_id"],
            ts=mandrill_data["ts"],
            message_ts=mandrill_data["message_ts"],
            subject=mandrill_data["subject"],
            email=mandrill_data["email"],
            sender=mandrill_data["sender"],
            state=mandrill_data["state"],
            message_id=mandrill_data["message_id"],
            time_opened=mandrill_data["time_opened"],
            time_clicked=mandrill_data["time_clicked"],
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
    except:
        return f"Something went wrong."


def save_data_to_db(mandrill_data: MandrillData, db: Session):
    """
    To prevent duplication of message objects in the database,
    - Try to obtain the data object asynchronously by message_id (primary key) to update the click and open times.
    - Create a new object if it does not exist in the database.
    """
    try:
        data = get_record_by_message_id(mandrill_data["message_id"], db)
        if data is None:
            create_db_record(mandrill_data, db)
    except:
        return f"Something went wrong."
