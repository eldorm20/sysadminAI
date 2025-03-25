SysAdmin AI - Task Automator


A command-line tool to automate and manage various system administration tasks, designed for SysAdmins and IT professionals. It includes both basic and pro-level features to help simplify your everyday system management tasks.

This tool allows you to:

Add or delete users

List users

Update and clean up the system

Monitor system performance

Backup and restore the system

Automate updates

Monitor system logs

Pro features (only available with a valid license key):

System Performance: Real-time system performance monitoring

Backup System: Create and restore system backups

Automate System Updates: Set up automatic system updates

Monitor Logs: Monitor and track system logs in real time



Features
Core Features
Add User: Add a new user to the system.

Delete User: Remove a user and optionally delete their home directory.

List Users: List all the users on the system.

Update System: Run system updates using apt.

Cleanup System: Clean unnecessary packages with apt autoremove.

Check Disk: Check disk usage with df.

Check Memory: Check available system memory with free.

Check CPU: Show CPU information using lscpu.

Pro Features (Requires License)
Check System Performance: View real-time system performance with top.

Backup System: Create a backup of your system using tar.

Restore Backup: Restore system from a backup.

Automate Updates: Set up unattended updates.

Monitor System Logs: Track logs in real time using journalctl.



Installation
Clone this repository to your local machine:
git clone https://github.com/eldorm20/sysadminAI.git
Navigate to the project directory:


cd sysadminAI
(Optional) Set up a virtual environment:


python3 -m venv venv
source venv/bin/activate
Install any required dependencies (if any):


pip install -r requirements.txt
You are ready to use SysAdmin AI.

Usage
Run the script:


python sysadminAI.py
The tool will prompt you for user input and allow you to select various system administration tasks. If you have a valid Pro license, you will also have access to the Pro features.

License Verification
When you first run the script, it will check for a valid license key (license.key) to unlock Pro features. If no license is found, it will prompt you to enter a license key.

License Key Format
The license key is a string with the format:

php-template
<license_key>,<expiration_date>,<status>
<license_key>: The unique key provided to you.
<expiration_date>: The expiration date of the license.
<status>: 1 for active, 0 for revoked.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributing
We welcome contributions to this project. If you'd like to improve this tool or add new features, feel free to fork the repository and submit a pull request.
Please make sure to follow the coding style and add tests for any new functionality.

Contact
For questions, suggestions, or help, feel free to open an issue on the GitHub repository or contact the project maintainers.

