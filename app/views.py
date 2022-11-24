from flask import Flask, render_template, request, redirect, url_for, flash, session

from . import app


@app.route('/')
def home():
    return render_template('index.html')