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
  "User": [ NODE
    {
      "Name": '', propertie
      "Email": '', properties
      "Tounge": '', propertie
      "Sex": '', label
      "Program_languages": '', properties
      "Nationalities": '', node
      "Projects": '', node
      "Team": '', relation
      "Role": '', node
      "Oficce_location": '', 
      "Age": '', label
      "Fav_movie": '',
      "OS": '', label
    }
  ],
  "Project": [ NODE
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