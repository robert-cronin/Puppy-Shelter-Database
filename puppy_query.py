from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from puppies import Base, Shelter, Puppy

engine = create_engine('sqlite:///puppyshelter.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# Part 1 - Query all of the puppies and return the results in ascending alphabetical order
# with engine.connect() as con:
#     rs = con.execute('SELECT name FROM Puppy ORDER BY Puppy.name desc')
#
#     for row in rs:
#         print row[0]

# Part 2 - Query all of the puppies that are less than 6 months old organized by the youngest first
# with engine.connect() as con:
#     rs = con.execute("SELECT dateOfBirth, name FROM Puppy WHERE dateOfBirth > '2016-10-08'")
#
#     for row in rs:
#         print row[0], row[1]

# Part 3 - Query all puppies by ascending weight
# with engine.connect() as con:
#     rs = con.execute("SELECT weight, name FROM Puppy ORDER BY weight asc")
#
#     for row in rs:
#         print row[0], row[1]

# Part 4 - Query all puppies grouped by the shelter in which they are staying
with engine.connect() as con:
    rs = con.execute("SELECT Shelter.name, Puppy.name FROM Puppy JOIN Shelter ORDER BY Shelter.name")

    for row in rs:
        print row[0], row[1]
