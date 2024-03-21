from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    resp = make_response(redirect(url_for('welcome')))
    resp.set_cookie('user', '%s:%s' % (name, email))
    return resp


@app.route('/welcome')
def welcome():
    user_cookie = request.cookies.get('user')
    if user_cookie:
        name, email = user_cookie.split(':')
        return render_template('welcome.html', name=name)
    else:
        return redirect(url_for('index'))


@app.route('/logout')
def logout():
    resp = make_response(redirect(url_for('index')))
    resp.set_cookie('user', '', expires=0)
    return resp


if __name__ == '__main__':
    app.run()
