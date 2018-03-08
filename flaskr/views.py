from flask import request ,redirect,url_for,render_template,flash, session,g
from flaskr import app,db
from flaskr.models import Entry, User

@app.route('/')
def show_entries():
    entries=Entry.query.order_by(Entry.id.desc()).all()
    return render_template('main_a.html', entries=entries)

@app.route('/add',methods=['POST'])
def add_entry():
    entry = Entry(
                  username = request.form['username'],
                  title = request.form['title'],
                  text = request.form['text'],
                  image = request.form['image'],
                  usernames = session['usernames']
                  )
    db.session.add(entry)
    db.session.commit()
    print(request.form['image'])
    flash("commited!!!")
    return redirect(url_for('show_entries'))

@app.route('/profile')
def profile_show():
    entries=Entry.query.order_by(Entry.id.desc()).all()
    return render_template('profile_a.html', entries=entries)


@app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        useruser = User.query.filter(User.username == request.form['username']).first()
        if useruser is None:
            user = User(
                        username = request.form['username'],
                        password = request.form['password']
                        )
            db.session.add(user)
            db.session.commit()
            print(request.form['username'],
            request.form['password'])
            # except IntegrityError:
                # flash("ユーザーがもういます")
                # return redirect(url_for('signup'))
            flash("ユーザー登録ができました！")
            return redirect(url_for('login'))
        else:
            flash('そのユーザー名は使われています。')
            return redirect(url_for('signup'))

    return render_template('signup_a.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        # user = User.query.order_by(User.id.desc()).all()
        user = User.query.filter(User.username == request.form['username']).first()
        print(user)
        if user is None:
            flash('ユーザー名が間違っています！')
            return redirect(url_for('login'))
        else:
            if user.password != request.form['password']:
                flash('パスワードが間違っています！')
                return redirect(url_for('login'))
            else:
                session['usernames'] = user.username
                # user = User.query.filter(User.username == request.form['username']).first()
                flash('ログインできました！')
                return redirect(url_for('show_entries'),)
        # sqlchemyはループを回すとき数字じゃなくて、言葉で！
        # print(user[0])
        # n = int(user[0].id)
        # m = n+1
        # # for i in range(m):
        #     # print('「'+str(i)+'」')
        #     if request.form['username'] == user[0].username:
            #         if request.form['password'] == user[i].password:
            #             flash('ログインできました！')
            #             return redirect(url_for('show_entries'))
            #         else:
            #             flash('パスワードが間違っています！')
            #             return redirect(url_for('login'))
            #     else:
            #         flash('ユーザー名が間違っています！')
            #         return redirect(url_for('login'))
    return render_template('login_a.html')

@app.route('/logout')
def logout():
    session.pop('usernames', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))
