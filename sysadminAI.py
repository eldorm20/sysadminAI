import os
import subprocess
from datetime import datetime

# Path to store the license file
LICENSE_FILE_PATH = "/home/elliot/devhub/license.key"

def check_license():
    """Check if the user has a valid license key for Pro features."""
    if not os.path.exists(LICENSE_FILE_PATH):
        # License file does not exist, ask for key
        print("No license found.")
        license_key = input("Enter your Pro license key: ").strip()
        # Store the license key, expiration date, and status
        with open(LICENSE_FILE_PATH, 'w') as file:
            file.write(f"{license_key},2026-03-24 02:52:20,1")  # Use the current license format
        print("License saved.")
        return False
    else:
        # License file exists, verify the key
        with open(LICENSE_FILE_PATH, 'r') as file:
            saved_license_data = file.read().strip()

        print(f"License found: {saved_license_data}")
        saved_license_key, saved_expiration_date, saved_status = saved_license_data.split(',')

        entered_license_key = input("Enter your Pro license key to verify: ").strip()

        if entered_license_key != saved_license_key:
            print("Invalid license key. Access to Pro features is restricted.")
            return False
        elif saved_status == '0':
            print("The license key has been revoked.")
            return False
        elif datetime.strptime(saved_expiration_date, "%Y-%m-%d %H:%M:%S") < datetime.now():
            print("The license key has expired.")
            return False
        else:
            print("License verified successfully.")
            return True


# Simulated SysAdmin tasks (Updated with real commands)
def add_user(username, password, sudo=False):
    print(f"Adding user: {username} with password: {password}")
    sudo_command = 'sudo' if sudo else ''
    command = f"{sudo_command} useradd -m -p {password} {username}"
    subprocess.run(command, shell=True, check=True)

def delete_user(username, delete_home=False):
    print(f"Deleting user: {username}")
    sudo_command = 'sudo'
    command = f"{sudo_command} userdel"
    if delete_home:
        command += f" -r {username}"
    else:
        command += f" {username}"
    subprocess.run(command, shell=True, check=True)

def list_users():
    print("Listing all users...")
    subprocess.run("cut -d: -f1 /etc/passwd", shell=True)

def update_system():
    print("Updating system...")
    subprocess.run("sudo apt update && sudo apt upgrade -y", shell=True)

def cleanup_system():
    print("Cleaning up system...")
    subprocess.run("sudo apt autoremove -y", shell=True)

def check_disk():
    print("Checking disk usage...")
    subprocess.run("df -h", shell=True)

def check_memory():
    print("Checking memory usage...")
    subprocess.run("free -h", shell=True)

def check_cpu():
    print("Checking CPU info...")
    subprocess.run("lscpu", shell=True)

# Pro Features (Updated with real commands)
def check_system_performance():
    print("Checking system performance...")
    subprocess.run("top -n 1", shell=True)

def backup_system():
    print("Creating system backup...")
    subprocess.run("sudo tar -czvf /home/elliot/system_backup.tar.gz /", shell=True)

def restore_backup():
    print("Restoring system from backup...")
    subprocess.run("sudo tar -xzvf /home/elliot/system_backup.tar.gz -C /", shell=True)

def automate_updates():
    print("Automating system updates...")
    try:
        subprocess.run("sudo apt install unattended-upgrades -y", shell=True, check=True)
        subprocess.run("sudo dpkg-reconfigure --priority=low unattended-upgrades", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error automating updates: {e}")

def monitor_system_logs():
    print("Monitoring system logs...")
    try:
        result = subprocess.run("sudo journalctl -f", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logs = result.stdout.decode('utf-8')
        if logs:
            print(logs)
        else:
            print("No logs found.")
    except subprocess.CalledProcessError as e:
        print(f"Error monitoring logs: {e}")

# Main Menu Function
def menu():
    """Display a CLI menu for SysAdmin tasks."""
    # Check if Pro license exists and is valid
    pro_license = check_license()

    while True:
        print("\n🎛️ SysAdmin AI - Task Automator")
        print("1. Add User")
        print("2. Delete User")
        print("3. List Users")
        print("4. Update System")
        print("5. Cleanup System")
        print("6. Check Disk")
        print("7. Check Memory")
        print("8. Check CPU")

        # Display Pro Feature if user has a valid license
        if pro_license:
            print("9. Check System Performance (Pro Feature)")
            print("10. Backup System (Pro Feature)")
            print("11. Restore from Backup (Pro Feature)")
            print("12. Automate System Updates (Pro Feature)")
            print("13. Monitor System Logs (Pro Feature)")

        print("14. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            sudo = input("Grant sudo privileges? (y/n): ").lower() == 'y'
            add_user(username, password, sudo=sudo)
        elif choice == '2':
            username = input("Enter username to delete: ")
            delete_home = input("Delete home directory? (y/n): ").lower() == 'y'
            delete_user(username, delete_home)
        elif choice == '3':
            list_users()
        elif choice == '4':
            update_system()
        elif choice == '5':
            cleanup_system()
        elif choice == '6':
            check_disk()
        elif choice == '7':
            check_memory()
        elif choice == '8':
            check_cpu()
        elif pro_license:
            # Pro Features
            if choice == '9':
                check_system_performance()
            elif choice == '10':
                backup_system()
            elif choice == '11':
                restore_backup()
            elif choice == '12':
                automate_updates()
            elif choice == '13':
                monitor_system_logs()
        elif choice == '14':
            print("Exiting SysAdmin AI. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
menu()
