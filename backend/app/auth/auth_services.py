from app.extensions import supabase

ALLOWED_ROLES = {"farmer", "transporter", "buyer"}

def signup_user(email: str, password: str, role: str) -> dict:
    """Creates a new user via Supabase Auth."""
    response = supabase.auth.sign_up({
        "email": email,
        "password": password,
        "options" : {
            "data" : {"role" : role}
        }
    })

    return {
        "user_id": response.user.id if response.user else None,
        "email": response.user.email if response.user else None,
        "role": response.user.user_metadata.get("role") if response.user else None,
        "session": response.session,
    }
