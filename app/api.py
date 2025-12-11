from flask import Flask, request, jsonify
from src.account_registry import AccountRegistry
from src.personal_account import PersonalAccount

app = Flask(__name__)
registry = AccountRegistry()

@app.post("/api/accounts")
def create_account():
    print("Request to create new account recieved")
    data = request.get_json()
    print(f"Create account request: {data}")

    if (registry.find(data["pesel"])):
        return jsonify({"message": "Account with this pesel already exists"}), 409
    
    account = PersonalAccount(data["first_name"], data["last_name"], data["pesel"])
    registry.add_account(account)
    return jsonify({"message": "Account created"}), 201


@app.get("/api/accounts")
def get_all_accounts():
    print("Get all accounts request received")
    accounts = registry.all_accounts()
    accounts_data = [{"first_name": acc.first_name, "last_name": acc.last_name, "pesel":
    acc.pesel, "balance": acc.balance} for acc in accounts]
    return jsonify(accounts_data), 200

@app.get("/api/accounts/count")
def get_account_count():
    print("Get account count request received")
    count = registry.count()
    return jsonify({"count": count}), 200

@app.get("/api/accounts/<pesel>")
def get_account_by_pesel(pesel):
    print("Get account by pesel request received")
    account = registry.find(pesel)
    if (not account):
        return jsonify({"error": "Account not found"}), 404
    return jsonify({"first_name": account.first_name, "last_name": account.last_name}), 200

# @app.route("/api/accounts/<pesel>", methods=['PATCH'])
@app.patch("/api/accounts/<pesel>")
def update_account(pesel):
    print("Patch account request received")
    account = registry.find(pesel)
    if (not account):
        return jsonify({"error": "Account not found"}), 404

    data = request.get_json()
    if (data["first_name"]):
        account.first_name = data["first_name"]
    if (data["last_name"]):
        account.last_name = data["last_name"]
    return jsonify({"message": "Account updated"}), 200

# @app.route("/api/accounts/<pesel>", methods=['DELETE'])
@app.delete("/api/accounts/<pesel>")
def delete_account(pesel):
    print("Delete account request received")
    if (not registry.find(pesel)):
        return jsonify({"error": "Account not found"}), 404

    registry.delete(pesel)
    return jsonify({"message": "Account deleted"}), 200