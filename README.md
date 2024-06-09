# CLI
# Grades CLI
This CLI tool allows you to retrieve your grades from the IIT Madras View grades portal. It simulates a login to the portal and then scrapes the grades from the resulting page.
## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/iit-madras-grades-cli.git
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ``
## Usage
1. Run the CLI:

   ```bash
   python cli.py
   ```

2. Enter your IIT Madras username and password when prompted.

3. For password, create a password.txt file and enter the password there.

4. The tool will attempt to log in and retrieve your grades. If successful, it will display your grades. Otherwise, it will show an error message.

## Notes
- This tool is provided as-is and may not work in all scenarios. Please report any issues or bugs to the repository.
- You may encounter certain problems while retrieving the data and parsing the HTML, for which you can edit the code for your own use and with respect to you command lin and run.
