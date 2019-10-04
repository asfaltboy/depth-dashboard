from flask import Flask
import request

app = Flask(__name__)

@app.route('/api/users')
def users():
    user_data = request.get_json()

@app.route('/api/project')
def projects():
    project_data = request.get_json()



if __name__ == '__main__':
    app.run()


'''
{
  "User": [
    {
      "Name": '',
      "Email": '',
      "Tounge": '',
      "Sex": '',
      "Program_languages": '',
      "Nationalities": '',
      "Projects": '',
      "Team": '',
      "Role": '',
      "Oficce_location": '',
      "Age": '',
      "Fav_movie": '',
      "OS": '',
    }
  ],
  "Project": [
    {
      "Languages": '',
      "Name": '',
      "vertical": '',
      "Hosting _rovider": '',
      "Services": '',
      "Jira": '',
    }
  ]
}

'''