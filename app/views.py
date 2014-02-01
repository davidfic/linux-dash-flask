from app import app
from app import data_gathering as dg
from flask import Flask
from flask import render_template





@app.route('/')
def index():
    return render_template("index.html",
        disk=dg.get_disk_usage(),
        os=dg.get_os(),
        ip=dg.get_ip(),
        uptime=dg.get_uptime(),
        ram=dg.get_ram())
