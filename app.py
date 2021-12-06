from flask import Flask, jsonify, request
from functools import wraps


app = Flask(__name__)


def error_check(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            result = f(*args, **kwargs)
        except Exception as e:
            error_message = e.args
            if not error_message:
                error_message = [e.description, ]
            return jsonify(status=500, message=error_message), 500
        return result

    return decorated_function


@app.route("/credit-policies", methods=["POST"])
@error_check
def credit_policies():
    if request.method == "POST" and request.is_json:
        data = request.json['data']
        response, message = check_credit(data)
        return jsonify(status=200, category=response, message=message)
    return jsonify(status=500, message="request is wrong.")


def check_credit(data):

    reasons = []
    is_accepted = True

    if data['customer_income'] < 500:
        reasons.append('LOW_INCOME')
        is_accepted = False

    if (data['customer_income']/2) < data['customer_debt']:
        reasons.append('HIGH_DEBT_FOR_INCOME')
        is_accepted = False

    if data['payment_remarks_12m'] > 0:
        reasons.append('PAYMENT_REMARKS_12M')
        is_accepted = False

    if data['payment_remarks'] > 1:
        reasons.append('PAYMENT_REMARKS')
        is_accepted = False

    if data['customer_age'] < 18:
        reasons.append('UNDERAGE')
        is_accepted = False   
        
    if is_accepted:
        results = "ACCEPT" 
        reasons = "credit check passed"

    else:
        results = "REJECT"

    return results, reasons



if __name__ == '__main__':
    app.run()
