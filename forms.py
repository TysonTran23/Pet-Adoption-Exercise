from flask_wtf import FlaskForm
from wtforms.validators import URL, InputRequired, NumberRange, Optional

from wtforms import (
    BooleanField,
    FloatField,
    IntegerField,
    RadioField,
    SelectField,
    StringField,
)


class AddPet(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField(
        "Species",
        validators=[InputRequired()],
        choices=[("cat", "Cats"), ("dog", "Dogs"), ("porcupine", "Porcupine")],
    )
    photo_url = StringField("Add a photo of the pet!", validators=[Optional(), URL()])
    age = IntegerField(
        "Age",
        validators=[Optional(), NumberRange(min=0, max=30)],
    )
    notes = StringField("Add notes")


class EditPet(FlaskForm):
    photo_url = StringField("Add a photo of the pet!", validators=[Optional(), URL()])
    notes = StringField("Add notes")
    available = SelectField(
        "Available", choices=[("True", "Available"), ("False", "Not Available")]
    )
