from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("calculator.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    number_one = request.form["number_one"]
    number_two = request.form["number_two"]
    operation = request.form["operation"]

    try:
        number_one = float(number_one)
        number_two = float(number_two)
    except ValueError:
        return render_template("calculator.html", result="Invalid input")

    result = None
    if operation == "add":
        result = number_one + number_two
    elif operation == "subtract":
        result = number_one - number_two
    elif operation == "multiply":
        result = number_one * number_two
    elif operation == "divide":
        if number_two == 0:
            result = "Cannot divide by zero"
        else:
            result = number_one / number_two

    return render_template("calculator.html", result=result)

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html", error=error), 404

@app.errorhandler(500)
def server_error(error):
    return render_template("500.html", error=error), 500

# Only run server when executed directly
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)