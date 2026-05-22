from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    all_sets = []

    # Generate numbers only when button is clicked
    if request.method == "POST":

        # Create 12 sets
        for s in range(12):

            # Generate 6 unique random numbers
            numbers = random.sample(range(1, 51), 6)

            # Sort numbers
            numbers.sort()

            # Add set to list
            all_sets.append(numbers)

    return render_template("index.html", sets=all_sets)

if __name__ == "__main__":
    app.run(debug=True)