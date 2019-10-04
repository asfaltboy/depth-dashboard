from flask import Flask
from flask import request
import json

app = Flask(__name__)

@app.route('/api/users')
def users():
    user_data = request.get_json()
    print(user_data)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

@app.route('/api/project')
def projects():
    project_data = request.json()



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