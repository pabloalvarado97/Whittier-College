from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_balance(data):
    balance = 0
    
    # Question 1
    if data["semester"] == "Fall 2023":
        balance += 24832
    elif data["semester"] == "Spring 2024":
        balance += 24832
    
    # Question 2
    if data["new_student"] == "Yes" and data["semester"] == "Fall 2023":
        balance += 200
    
    # Question 3
    credit_hours = int(data["credit_hours"])
    if 12 <= credit_hours <= 17:
        pass
    elif credit_hours > 17:
        balance = balance +  (credit_hours - 17)*2038.50
    else:
        balance = balance - 24832 +  credit_hours * 2038.50
    
    # Question 4
    total_class_fees = float(data["total_class_fees"]) if data["total_class_fees"] else 0.0
    balance += total_class_fees
    
    # Question 5
    if data["living_location"] == "On-campus: Single room":
        balance += 4847
    elif data["living_location"] == "On-campus: Double room":
        balance += 4190
    elif data["living_location"] == "On-campus: Triple room":
        balance += 3339
    
    # Question 6
    if data["meal_plan"] == "19 Meals":
        balance += 3446
    elif data["meal_plan"] == "19 Meals with Flex":
        balance += 3666
    elif data["meal_plan"] == "15 Meals":
        balance += 3321
    elif data["meal_plan"] == "15 Meals with Flex":
        balance += 3541
    elif data["meal_plan"] == "10 Meals":
        balance += 3119
    elif data["meal_plan"] == "10 Meals with Flex":
        balance += 3339
    elif data["meal_plan"] == "5 Meals":
        balance += 1207
    elif data["meal_plan"] == "5 Meals with Flex":
        balance += 1317
    
    # Question 7
    if data["health_insurance"] == "Yes" and data["semester"] == "Fall 2023":
        balance += 653.33
    elif data["health_insurance"] == "Yes" and data["semester"] == "Spring 2024":
        balance += 844.67
    
    # Question 8
    #total_financial_aid = float(data["total_financial_aid"]) if data["total_financial_aid"] else 0.0
    financial_aid_a = float(data["financial_aid_a"]) if data["financial_aid_a"] else 0.0
    financial_aid_b = float(data["financial_aid_b"]) if data["financial_aid_b"] else 0.0
    financial_aid_c = float(data["financial_aid_c"]) if data["financial_aid_c"] else 0.0
    financial_aid_d = float(data["financial_aid_d"]) if data["financial_aid_d"] else 0.0
    financial_aid_e = float(data["financial_aid_e"]) if data["financial_aid_e"] else 0.0
    total_financial_aid = financial_aid_a + financial_aid_b + financial_aid_c + financial_aid_d + financial_aid_e

    balance -= total_financial_aid
    
    #Question 9
    previous_balance = float(data["previous_balance"]) if data["previous_balance"] else 0.0
    balance += previous_balance
    
    balance = "{:,.2f}".format(balance)
    return balance

@app.route("/", methods=["GET", "POST"])
def index():
    balance = None

    if request.method == "POST":
        data = {
            "semester": request.form.get("semester"),
            "new_student": request.form.get("new_student"),
            "credit_hours": request.form.get("credit_hours"),
            "total_class_fees": request.form.get("total_class_fees"),
            "living_location": request.form.get("living_location"),
            "meal_plan": request.form.get("meal_plan"),
            "health_insurance": request.form.get("health_insurance"),
            #"total_financial_aid": request.form.get("total_financial_aid"),
            "financial_aid_a": request.form.get("financial_aid_a"),
            "financial_aid_b": request.form.get("financial_aid_b"),
            "financial_aid_c": request.form.get("financial_aid_c"),
            "financial_aid_d": request.form.get("financial_aid_d"),
            "financial_aid_e": request.form.get("financial_aid_e"),
            "previous_balance": request.form.get("previous_balance"),
        }

        balance = calculate_balance(data)

    return render_template("index.html", balance=balance)

if __name__ == "__main__":
    app.run(debug=True)