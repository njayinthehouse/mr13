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

genres = Table('genres', metadata,
               Column('id', Integer, primary_key=True),
               Column('value', String(256), unique=True)
               )

genre_mappings = Table('genremappings', metadata,
                       Column('id', Integer, primary_key=True),
                       Column('manga_id', None, ForeignKey('manga.id')),
                       Column('genre_id', None, ForeignKey('genres.id'))
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

# Hard coded values
connection = engine.connect()
connection.execute(genres.insert(), [
    {'id': 1, 'value': 'Action'},
    {'id': 2, 'value': 'Adventure'},
    {'id': 3, 'value': 'Comedy'},
    {'id': 4, 'value': 'Demons'},
    {'id': 5, 'value': 'Drama'},
    {'id': 6, 'value': 'Ecchi'},
    {'id': 7, 'value': 'Fantasy'},
    {'id': 8, 'value': 'Gender Bender'},
    {'id': 9, 'value': 'Harem'},
    {'id': 10, 'value': 'Historical'},
    {'id': 11, 'value': 'Horror'},
    {'id': 12, 'value': 'Josei'},
    {'id': 13, 'value': 'Magic'},
    {'id': 14, 'value': 'Martial Arts'},
    {'id': 15, 'value': 'Mature'},
    {'id': 16, 'value': 'Mecha'},
    {'id': 17, 'value': 'Military'},
    {'id': 18, 'value': 'Mystery'},
    {'id': 19, 'value': 'One Shot'},
    {'id': 20, 'value': 'Psychological'},
    {'id': 21, 'value': 'Romance'},
    {'id': 22, 'value': 'School Life'},
    {'id': 23, 'value': 'Sci-Fi'},
    {'id': 24, 'value': 'Seinen'},
    {'id': 25, 'value': 'Shoujo'},
    {'id': 26, 'value': 'Shoujoai'},
    {'id': 27, 'value': 'Shounen'},
    {'id': 28, 'value': 'Shounenai'},
    {'id': 29, 'value': 'Slice of Life'},
    {'id': 30, 'value': 'Smut'},
    {'id': 31, 'value': 'Sports'},
    {'id': 32, 'value': 'Super Power'},
    {'id': 33, 'value': 'Supernatural'},
    {'id': 34, 'value': 'Tragedy'},
    {'id': 35, 'value': 'Vampire'},
    {'id': 36, 'value': 'Yaoi'},
    {'id': 37, 'value': 'Yuri'},
])