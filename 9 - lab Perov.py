from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
db = SQLAlchemy(app)

# Модель данных
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    link = db.Column(db.String(200))

    def init(self, title, link):
        self.title = title
        self.link = link

# Главная страница
@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)

# Добавление проекта
@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    link = request.form['link']
    project = Project(title, link)
    db.session.add(project)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

