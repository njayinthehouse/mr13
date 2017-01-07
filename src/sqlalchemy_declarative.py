# Just to define SQLite tables
from sqlalchemy import create_engine, Table, Column, Integer, String, Text, Boolean, Date, MetaData, ForeignKey

engine = create_engine('sqlite:///manga.db')
metadata = MetaData()

manga = Table('manga', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String(256), unique=True),
              Column('author', String(256)),
              Column('artist', String(256)),
              Column('year_of_release', String(8)),
              Column('ongoing', Boolean),
              Column('summary', Text)
              )

genre_mappings = Table('genremappings', metadata,
                       Column('id', Integer, primary_key=True),
                       Column('manga_id', None, ForeignKey('manga.id')),
                       Column('genre_id', None, Integer)
                       )

chapters = Table('chapters', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('manga_id', None, ForeignKey('manga.id')),
                 Column('number', Integer, nullable=False),
                 Column('name', String(256), nullable=False),
                 Column('date_of_release', Date, nullable=False),
                 Column('is_in_stash', Boolean, default=False)
                 )

tracking = Table('tracking', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('manga_id', None, ForeignKey('manga.id'))
                 )

metadata.create_all(engine)