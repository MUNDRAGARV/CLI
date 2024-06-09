import typer
import requests
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


app = typer.Typer()

def login_to_portal(username: str, password: str, login_url: str, session: requests.Session) -> bool:
    login_data = {
        'username': username,
        'password': password
    }
    response = session.post(login_url, data=login_data)
    return response.ok

def retrieve_grades_and_cgpa(grades_url: str, session: requests.Session):
    response = session.get(grades_url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        #grades are in a table with class 'slotwise'
        grades_table = soup.find('table', class_='slotwise')
        if grades_table:
            grades = []
            for row in grades_table.find_all('tr'):
                #grades is in the sixth column of each row
                grade = row.find_all('td')[5].text.strip()
                grades.append(grade)
        # CGPA is in a div with id 'slotwise'
        #cgpa_element = soup.find('div', id='slotwise')
        #cgpa = cgpa_element.text.strip() if cgpa_element else None
        #return grades, cgpa
        return grades
    else:
        typer.echo("Failed to retrieve grades.")
        raise typer.Exit(code=1)


@app.command()
def get_grades(username: str = typer.Option(..., prompt=True, help="Your IIT Madras username")):
    with open("password.txt", "r") as file:
        password = file.read().strip()

    grades_url = 'https://www.iitm.ac.in/viewgrades/viewgrades.php'
    login_url = 'https://www.iitm.ac.in/viewgrades/index.php'
    
    with requests.Session() as session:
        session.verify=False
        if login_to_portal(username, password, login_url, session):
            grades= retrieve_grades_and_cgpa(grades_url, session)
            typer.echo(f"Grades: {grades}")
        else:
            typer.echo("Login failed. Please check your credentials.")

if __name__ == "__main__":
    app()
