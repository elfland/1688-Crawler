from flask import g, request, jsonify

from . import web
from app.cache.redis import RedisClient


def get_redis_conn():
    if not hasattr(g, 'redis'):
        g.redis = RedisClient()
    return g.redis


@web.route('/', methods=['GET'])
def index():
    return '<h1 style="text-align: center; margin-top: 100px;">1688-Crawler based on Flask</h1>'


@web.route('/proxy-cookies/add', methods=['POST'])
def add_proxy_cookies():
    conn = get_redis_conn()
    is_success = conn.add(request.form.get('cookie'))
    res = {'msg': '录入成功'} if is_success else {'errcode': 500, 'errmsg': '录入失败'}
    return jsonify(res)
