
from flask.ext.wtf import form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email

class LoginForm(form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)