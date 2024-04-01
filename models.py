from sqlalchemy import Column, String
from sqlmodel import Field, Relationship, SQLModel
from datetime import datetime

class Store(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(sa_column=Column("name", String(255)))
    owner: str = Field(sa_column=Column("owner", String(255)))
    enabled: bool
    balance: float
    currency: str = Field(sa_column=Column("currency", String(255)))
    offers: list["Offer"] = Relationship(back_populates="store")
    timestamp: datetime

class Offer(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    buying: bool
    itemname: str = Field(sa_column=Column("itemname", String(255)))
    limit: int
    maxNumWanted: int
    minDurability: float
    price: float
    quantity: int
    store_id: int | None = Field(default=None, foreign_key="store.id")
    store: Store = Relationship(back_populates="offers")
    timestamp: datetime