from flask import Blueprint, render_template, jsonify, request
from app.bot import CookieClickerBot

bp = Blueprint('main', __name__)
bot = CookieClickerBot()

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/click', methods=['POST'])
def click():
    bot.click()
    return jsonify(success=True, cookies=bot.cookies)

@bp.route('/status')
def status():
    return jsonify(cookies=bot.cookies)