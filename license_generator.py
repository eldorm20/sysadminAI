import secrets
from datetime import datetime, timedelta

LICENSE_FILE = "license.key"

def generate_license_key():
    """Generates a new license key in format PRO-XXXXXXXXXX."""
    return "PRO-" + ''.join(secrets.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for _ in range(10))

def create_license_file():
    """Creates a file and writes the first license."""
    license_key = generate_license_key()
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    expires_at = (datetime.now() + timedelta(days=365)).strftime("%Y-%m-%d %H:%M:%S")
    status = 1  # 1 means active, 0 means revoked

    with open(LICENSE_FILE, 'w') as file:
        file.write(f"{license_key},{expires_at},{status}\n")

    print(f"✅ License Key Generated: {license_key}")
    print(f"🔐 The license key has been stored in {LICENSE_FILE}.")

def revoke_license_key():
    """Revokes the license key by changing the status to 0 (inactive)."""
    try:
        with open(LICENSE_FILE, 'r') as file:
            license_data = file.readlines()

        if not license_data:
            print("❌ No license found to revoke.")
            return

        license_key, expires_at, status = license_data[0].strip().split(',')

        if status == '0':
            print("❌ License is already revoked.")
            return

        # Revoke the license
        with open(LICENSE_FILE, 'w') as file:
            file.write(f"{license_key},{expires_at},0\n")

        print(f"❌ License {license_key} has been revoked.")
    except Exception as e:
        print(f"⚠️ Error while revoking license: {e}")

def validate_license_key(key):
    """Validates a license key by checking its validity from the file."""
    try:
        with open(LICENSE_FILE, 'r') as file:
            license_data = file.readlines()

        if not license_data:
            print("❌ No license found.")
            return

        license_key, expires_at, status = license_data[0].strip().split(',')

        if key != license_key:
            print("❌ Invalid License Key!")
            return

        if datetime.strptime(expires_at, "%Y-%m-%d %H:%M:%S") < datetime.now():
            print("⏳ License key is expired!")
            return

        if status == '0':
            print("🚫 License key has been revoked!")
            return

        print("✅ License key is valid!")

    except Exception as e:
        print(f"⚠️ Error validating license: {e}")

# Run script
if __name__ == "__main__":
    create_license_file()  # Ensure the license file is created with a new license key
    # Optionally, you can revoke the license after some time by calling revoke_license_key()
