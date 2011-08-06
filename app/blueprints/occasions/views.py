# -*- coding: utf-8 -*-

from flask import flash, request, session, redirect, url_for, render_template
from google.appengine.api import users

from auth import login_required
from occasions import occasions_bp as bp
from models import OccasionForm, Occasion
from slugify import slugify

@bp.route('/add', methods = ['GET', 'POST'])
@login_required
def add():
    """Display a form for adding a new occasion"""
    form = OccasionForm()
    if form.validate_on_submit():
        occasion = Occasion(key_name=slugify(form.title.data),
                            title = form.title.data,
                            description = form.description.data,
                            date_start = form.date_start.data,
                            date_end = form.date_end.data,
                            author = users.get_current_user())
        occasion.put()
        flash(slugify(form.title.data))
        return redirect(url_for('occasions.list'))
    return render_template('add.html', form=form)

@bp.route('/<key_name>/edit', methods = ['GET', 'POST'])
@login_required
def edit(key_name):
    """Display a form for editing or deleting an existing occasion"""
    form = OccasionForm()
    occasion = Occasion.get_by_key_name(key_name)
    if not occasion.author == session['user']:
        flash('access denied')
        return redirect(url_for('occasions.view', key_name=occasion.key().id_or_name()))
    if form.validate_on_submit():
        if form.delete.data:
            occasion.delete()
            return redirect(url_for('occasions.list'))
        occasion.title=form.title.data
        occasion.description=form.description.data
        occasion.date_start=form.date_start.data
        occasion.date_end=form.date_end.data
        flash(form.delete.data)
        return redirect(url_for('occasions.view', key_name=occasion.key().id_or_name()))
    form.title.data=occasion.title
    form.description.data=occasion.description
    form.date_start.data=occasion.date_start
    form.date_end.data=occasion.date_end
    flash(occasion.date_start)
    return render_template('edit.html', occasion=occasion, form=form)

@bp.route('/')
def list():
    """Displays a list of occasions"""
    occasions = Occasion.all()
    return render_template('list.html', occasions=occasions)

@bp.route('/<key_name>/')
def view(key_name):
    """Displays a list of occasions"""
    occasion = Occasion.get_by_key_name(key_name)
    return render_template('view.html', occasion=occasion)