
from flask import Flask, render_template

app = Flask(
    __name__,
    static_folder="public/static",
    static_url_path="/static"
)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/farmer")
def farmer():
    return render_template("farmer/dashboard.html")

@app.route("/farmer/my_produce")
def farmer_my_produce():
    return render_template("farmer/my_produce.html")

@app.route("/farmer/orders")
def farmer_orders():
    return render_template("farmer/orders.html")

@app.route("/farmer/ai_assistant")
def farmer_ai_assistant():
    return render_template("farmer/ai_assistant.html")

@app.route("/farmer/analytics")
def farmer_analytics():
    return render_template("farmer/analytics.html")

@app.route("/farmer/add_produce")
def add_produce():
    return render_template("farmer/add_produce.html")


@app.route("/farmer/edit_produce")
def edit_produce():
    return render_template("farmer/edit_produce.html")


@app.route("/farmer/messages")
def farmer_messages():
    return render_template("farmer/messages.html")

@app.route("/farmer/profile")
def farmer_profile():
    return render_template("farmer/profile.html")

@app.route("/farmer/settings")
def farmer_settings():
    return render_template("farmer/settings.html")



@app.route("/buyer")
def buyer():
    return render_template("buyer/dashboard.html")

@app.route("/buyer/marketplace")
def marketplace():
    return render_template("buyer/marketplace.html")

@app.route("/buyer/product_details")
def buyer_product_details():
    return render_template("buyer/product_details.html")

@app.route("/buyer/cart")
def buyer_cart():
    return render_template("buyer/cart.html")

@app.route("/buyer/checkout")
def buyer_checkout():
    return render_template("buyer/checkout.html")

@app.route("/buyer/orders")
def buyer_orders():
    return render_template("buyer/orders.html")

@app.route("/buyer/tracking")
def buyer_tracking():
    return render_template("buyer/tracking.html")

@app.route("/transporter")
def transporter():
    return render_template("transporter/dashboard.html")

@app.route("/transporter/deliveries")
def transporter_deliveries():
    return render_template("transporter/deliveries.html")


@app.route("/transporter/tracking")
def transporter_tracking():
    return render_template("transporter/tracking.html")


@app.route("/transporter/confirmation")
def transporter_confirmation():
    return render_template("transporter/confirmation.html")


@app.route("/transporter/profile")
def transporter_profile():
    return render_template("transporter/profile.html")


@app.route("/transporter/settings")
def transporter_settings():
    return render_template("transporter/settings.html")


@app.route("/admin")
def admin():
    return render_template("admin/dashboard.html")

@app.route("/admin/users")
def admin_users():
    return render_template("admin/users.html")


@app.route("/admin/farmers")
def admin_farmers():
    return render_template("admin/farmers.html")


@app.route("/admin/orders")
def admin_orders():
    return render_template("admin/orders.html")


@app.route("/admin/analytics")
def admin_analytics():
    return render_template("admin/analytics.html")


@app.route("/admin/settings")
def admin_settings():
    return render_template("admin/settings.html")

if __name__ == "__main__":
    app.run(debug=True)



