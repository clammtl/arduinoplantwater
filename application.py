import os
import re
from flask import Flask, jsonify, render_template, request, redirect


# Configure application
app = Flask(__name__)



# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    """Render index"""
    return render_template("index.html")

@app.route("/readme")
def readme():
    """Render readme page"""
    return render_template("readme.html")

@app.route("/data")
def data():
    """Render data"""
    return render_template("data.html")

@app.route("/chart")
def chart():
    """Render chart"""
    return render_template("chart.html")

@app.route("/design")
def design():
    """Render design page"""
    return render_template("design.html")

@app.route("/arduino")
def arduino():
    """Render arduino code page"""
    return render_template("arduino.html")