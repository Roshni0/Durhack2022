from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import pandas
import csv
from sell import start_model, run_model
from twilio.rest import Client

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db?check_same_thread=False"
db = SQLAlchemy(app)


class House(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    num_bedrooms = db.Column(db.Float, nullable=False)
    website = db.Column(db.String(500), nullable=False)
    sqrft = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<House %r>" % self.id

@app.route("/sell", methods=["POST", "GET"])
def sell():
    if request.method == "POST":
        num_bedroom = request.form["bedroom"]
        house_type = request.form["house"]
        result = run_model(num_bedroom, house_type)
        return render_template("sell.html", result=result)
    else:
        return render_template("sell.html")

@app.route("/buy", methods=["POST", "GET"])
def buy():
    if request.method == "POST":
        num_bedroom = request.form["bedroom"]
        house_type = request.form["house"]
        result = run_model(num_bedroom, house_type)
        return render_template("buy.html", result=result)
    else:
        return render_template("buy.html", houses=houses)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        houses_list = request.data["lists"]
        for house in houses_list:
            new_house = House(
                price=house_price,
                location=house_location,
                num_bedrooms=house_num_bedrooms,
                website=website,
                sqrft=sqrft,
            )

        try:
            db.session.add(new_house)
            db.session.commit()
            return redirect("/")
        except:
            return "There was an issue adding your house"

    else:
        tasks = House.query.order_by(House.price).all()
        print(houses[0].num_bedrooms)
        return render_template("home.html")


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



RESULTS = []

with open("output.csv", "r") as file:
    csvreader = csv.reader(file)
    headers = next(csvreader)

    for row in csvreader:
        if row[7] == "":
            continue
        if row[1] == "":
            row[1] = "POA"
        new_house = House(
            price=row[1],
            location=row[3],
            num_bedrooms=float(row[7]),
            website=row[5],
            sqrft=500,
        )
        try:
            db.session.add(new_house)
            db.session.commit()
        except:
            "There was an issue adding your house"
        RESULTS.append(new_house)
        # print(new_house)

    houses = RESULTS

if __name__ == "__main__":
    start_model()
    account_sid = "AC394c8552d6cb33f1aba9ad1d59afc9c6"
    auth_token = "094665b76f68ccd98314e0dc6cc59456"
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body="Hey Bob! New property available! Click Here https://www.rightmove.co.uk/properties/120207362#/?channel=RES_BUY",
                        from_='+19035277790',
                        to='+447776450115'
                    )
    print(message.sid)
    app.run(debug=True)
