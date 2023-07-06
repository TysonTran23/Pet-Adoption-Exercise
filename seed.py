from app import app
from models import Pet, db

db.drop_all()
db.create_all()

default_url = "https://media.istockphoto.com/id/1399660843/vector/happy-children-at-the-zoo.jpg?s=612x612&w=0&k=20&c=2Tlm-fVcw4FWtdeMl_Sr9bi3G1rKfPg35m3aUB0dHmU="

pet1 = Pet(
    name="Flacko",
    species="Dragon",
    photo_url=default_url,
    age=100,
    notes="From game of thrones",
)

pet2 = Pet(
    name="Simon",
    species="Cat",
    photo_url=default_url,
    age=3,
    notes="TikTok Famous",
    available=False,
)

pet3 = Pet(
    name="Mojo",
    species="Dog",
    photo_url=default_url,
    age=16,
    notes="Likes rice",
    available=False,
)

pet4 = Pet(
    name="John",
    species="Elephant",
    photo_url=default_url,
    age=100,
    notes="From game of thrones",
)

pet5 = Pet(
    name="Pseudo",
    species="Cricket",
    photo_url=default_url,
    age=1,
    notes="From the garden",
)

db.session.add_all([pet1, pet2, pet3, pet4, pet5])
db.session.commit()
