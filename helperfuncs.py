import json
import asyncio
from api_data_manager import process_data, get_api_data, save_data_to_db


async def send_data_to_frontend(websocket, db):
    """Display live data from Mandrill API and save it to the database"""
    await websocket.accept()

    while True:
        try:
            api_data = await get_api_data()
            response_details = process_data(api_data)

            # Send data to the frontend
            await websocket.send_text(json.dumps(response_details))

            save_data_to_db(response_details, db)

            # using asyncio.sleep as a rate limiter of messages parsed per instance
            await asyncio.sleep(1)

        except:
            await websocket.send_text("Something went wrong.")
            break
