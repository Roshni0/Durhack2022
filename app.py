from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class House(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(200), nullable=False)
    num_bedrooms = db.Column(db.Integer, nullable=False)
    website = db.Column(db.String(500), nullable=False)
    sqrft = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<House %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        house_price = request.form['price']
        house_location = request.form['location']
        house_num_bedrooms = request.form['house_num_bedrooms']
        website = request.form['website']
        sqrft = request.form['sqrft']

        new_house = House(price=house_price, location=house_location, num_bedrooms=house_num_bedrooms, website=website, sqrft=sqrft)

        try:
            db.session.add(new_house)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your house'

    else:
        tasks = House.query.order_by(House.price).all()
        return render_template('index.html', tasks=tasks)


# @app.route('/update/<int:id>', methods=['GET', 'POST'])
# def update(id):
#     task = House.query.get_or_404(id)
#     if request.method == 'POST':
#         task.content = request.form['content']

#         try:
#             db.session.commit()
#             return redirect('/')
#         except:
#             return 'There was an issue updating your task'

#     else:
#         return render_template('update.html', task=task)


if __name__ == "__main__":
    app.run(debug=True)