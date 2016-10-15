from flask import Flask, render_template, json, redirect, request
from model.author import *
from db.db_method import *
from lib.pagecreate import Pagination

app = Flask(__name__)


class NonASCIIJsonEncoder(json.JSONEncoder):
    def __init__(self, **kwargs):
        kwargs['ensure_ascii'] = False
        super(NonASCIIJsonEncoder, self).__init__(**kwargs)
app.json_encoder = NonASCIIJsonEncoder


@app.route('/')
@app.route('/page/<int:p>/')
@app.route('/page/')
def page(p=1):
    conn = connect('127.0.0.1', 'root', 'root', 'wechat_article')
    sql = "select * from article ORDER by -post_time"
    result = get(conn, sql)
    page_list = Pagination(p, 10, result)
    has_next = page_list.has_next
    has_prev = page_list.has_prev
    pager = page_list.pager
    page = page_list.page
    data = page_list.items
    return render_template('pagecreate.html',
                           has_next=has_next,
                           has_prev=has_prev,
                           pager=pager,
                           page=page,
                           data=data)


@app.route('/blog/')
def blog():
    return redirect('http://blog.wususu.cn')


@app.route('/post/', methods=['POST', 'GET'])
def post():
    if request.method == 'POST':
        type = request.form.get('value1')
        id = request.form.get('value2')
        flag = 0
        if type == 'wechat':
            flag = 1
        elif type == 'jianshu':
            flag = 2
        elif type == 'wangyi':
            flag = 3
        new = AuthorUser(id, 'wususu', flag)
        db.session.add(new)
        try:
            db.session.commit()
        except Exception as e:
            pass
    return render_template('author_form.html')


@app.route('/myread/')
def myread():
    my_read = AuthorUser.query.filter_by(username='wususu').all()
    return render_template('my_read.html', authors=my_read)


if __name__ == '__main__':
    app.debug = True
    app.run(host="127.0.0.4")
