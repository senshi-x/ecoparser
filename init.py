import requests
import json
from sqlmodel import Session
from database import create_db_and_tables, engine

from models import Offer, Store
from datetime import datetime

# TODO: Handle uniqueness to prevent duplicates (only one store/offer/timestamp combination)

def updateDB():
    data_store = requests.get("https://white-tiger.play.eco/api/v1/plugins/EcoPriceCalculator/stores").json()["Stores"]

    now = datetime.now()
    with Session(engine) as session:
        for store in data_store:
            print(json.dumps(store, indent=4, sort_keys=True))
            store["Balance"] = 9999999 if store["Balance"] == "Infinity" else store["Balance"]
            store_db = Store(
                balance   = store["Balance"],
                currency  = store["CurrencyName"],
                enabled   = store["Enabled"],
                name      = store["Name"],
                owner     = store["Owner"],
                timestamp = now)
            session.add(store_db)
            session.commit() # must commit here so we can use the store id for FK
            for offer in store["AllOffers"]:
                session.add(Offer(
                    buying        = offer["Buying"],
                    itemname      = offer["ItemName"],
                    price         = offer["Price"],
                    quantity      = offer["Quantity"],
                    limit         = offer["Limit"],
                    maxNumWanted  = offer["MaxNumWanted"],
                    minDurability = offer["MinDurability"],
                    store_id      = store_db.id,
                    timestamp     = now))

        session.commit()

def main():
    create_db_and_tables()
    updateDB()


if __name__ == "__main__":
    main()