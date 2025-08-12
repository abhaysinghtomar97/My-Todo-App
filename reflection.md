render_template('index.html') --> to render html by "import flask from render_template

to activate --> .\env\Scripts\activate.ps1

sql-alchemy --> facilitate to manage database through python -pip install flask-sqlalchemy       

SQL lite Viewer --> to read database files

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///todo.db" => to add DB file in Folder

jinja --> to 

<form action="/" method="POST"  class="p-5"> -- >used to GET or POST data

to Create New DB File :- 
        >>python
        >>from app import app, db
        >>> with app.app_context():
        ...     db.create_all()
        ...

 app.run(debug=True,port=8000) 

    if debug =True == >Exact Error Will Show  => for developers
    if debug =False ==> Random "Internal Error" => for users