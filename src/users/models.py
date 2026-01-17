from sqlmodel import SQLModel, Column, Field
import uuid
from datetime import datetime
import sqlalchemy.dialects.postgresql as pg


class User(SQLModel, table=True):
    __tablename__ = 'users'

    uid:uuid.UUID = Field(
        sa_column=Column(
            pg.UUID(as_uuid=True),
            nullable=False,
            primary_key=True,
            default=uuid.uuid4
        )
    )
    name:str = Field(
        sa_column=Column(
            pg.VARCHAR,
            nullable=False,
            default='User'
        )
    )
    username:str = Field(
        sa_column=Column(
            pg.VARCHAR,
            nullable=False,
            unique=True
        )
    )
    email:str = Field(
        sa_column=Column(
            pg.VARCHAR,
            nullable=False,
            unique=True
        )
    )
    role:str = Field(
        sa_column=Column(
            pg.VARCHAR,
            nullable=False,
            default='User'
        )
    )
    active:bool = Field(
        sa_column=Column(
            pg.BOOLEAN,
            nullable=False,
            default=False
        )
    )
    login_count:int = Field(
        sa_column=Column(
            pg.INTEGER, 
            default=0
        )
    )
    created_at:datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP, 
            default=datetime.now
        )
    )
    updated_at:datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP, 
            default=datetime.now
        )
    )


    def __repr__(self):
        return f"<User {self.name}>"