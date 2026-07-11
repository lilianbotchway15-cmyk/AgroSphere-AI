from flask import Flask, request, jsonify
from supabase_auth.errors import AuthApiError
from app.auth.auth_services import signup_user, ALLOWED_ROLES

app = Flask(__name__)


@app.post("/api/auth/signup")
def signup():
    data = request.get_json(silent=True) or {}
    email = data.get("email")
    password = data.get("password")
    role = data.get("role")


    if not email or not password:
        return jsonify({"error": "email and password are required"}), 400

    if role not in ALLOWED_ROLES:
        return jsonify({"error": f"role must be one of {sorted(ALLOWED_ROLES)}"}), 400

    try:
        result = signup_user(email, password, role)
    except AuthApiError as e:
        return jsonify({"error": e.message}), e.status

    return jsonify(result), 201


if __name__ == "__main__":
    app.run(debug=True, port=5001)
