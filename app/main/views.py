from flask import render_template, request, redirect, url_for, abort
from . import main
from flask_login import login_required, current_user
from app.templates.models import User, PitchCategory, Pitches, Comments, Likes, Dislikes
from .forms import UpdateProfile, PitchForm, CommentForm, CategoriesForm
from .. import db, photos

@main.route('/')
def index():
    """View root page function that returns index page and the various news sources"""

    title = 'Home- Welcome to the Pitch Website'
    categories = PitchCategory.get_categories()

    return render_template('index.html', title=title, categories=categories)


# Route for adding a new pitch

@main.route('/category/pitch/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_pitch(id):
    '''
    Function to check Pitches form
    '''
    form = PitchForm()
    category = PitchCategory.query.filter_by(id=id).first()

    if category is None:
        abort(404)
