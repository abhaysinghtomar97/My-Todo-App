from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db =SQLAlchemy(app)

# DataBase 
class Todo(db.Model):
    sno =db.Column(db.Integer,primary_key=True)
    title =db.Column(db.String,primary_key=False)
    desc=db.Column(db.String,primary_key=False)
    date_created =db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return F"{self.sno}-{self.title}"


@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        title =request.form['title']
        desc = request.form['desc']
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
    
    allTodo = Todo.query.all()
    return render_template('index.html', allTodo=allTodo)


@app.route("/about")
def about():
    return "<p>I'm Btech Student , pursuing from PSIT Kanpur Looking Forward to Explore New technologies and Much more!</p>"


@app.route('/show')
def products():
    allTodo =Todo.query.all()
    print(allTodo)
    return 'This is All Todos'

@app.route('/update/<int:sno>',  methods=['GET', 'POST'])
def update(sno):
    if request.method=='POST':
        title =request.form['title']
        desc = request.form['desc']
        todo =Todo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect('/')

    todo =Todo.query.filter_by(sno=sno).first()
    return render_template('update.html', todo=todo)

@app.route('/delete/<int:sno>')
def delete(sno):
    todo =Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

if __name__ =="__main__":
    app.run(debug=True,port=8000)