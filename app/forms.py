from flask_uploads import UploadSet, IMAGES
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired

images = UploadSet('images', IMAGES)

class UploadForm(FlaskForm):
    photo = FileField('image', validators=[
        FileRequired(),
        FileAllowed(images, 'Images only!')
    ])
    description = StringField('Description', validators = [InputRequired()])