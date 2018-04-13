from flask import render_template, request, flash
from . import app
from .forms import WatcherForm


@app.route("/", methods=['GET', 'POST'])
def home():
    form = WatcherForm()
    if request.method == 'POST' and form.validate_on_submit():
        flash('Successfull created a watcher')
        # print(form.data)
    context = {
        'form': form
    }
    return render_template('home.html', **context)
