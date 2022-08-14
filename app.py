from flask import Flask, render_template, request,redirect,url_for,jsonify,abort
from flask_sqlalchemy import SQLAlchemy
import sys

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Sylvasam18@localhost:5432/todoapp'
db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    
    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'
    
db.create_all()

# @app.route('/todos/create', methods=['POST'])
# def create_todo():
#    description = request.get_json()['description']
#    todo = Todo(description=description)
#    db.session.add(todo)
#    db.session.commit();
#    return jsonify({
#         'description': todo.description
#      })

@app.route('/todos/create', methods=['POST'])
def create_todo():   
   body={}
   error = False
   try: 
       description =  request.get_json()['description']
       todo = Todo(description=description)
       body['description'] = todo.description
       db.session.add(todo)
       db.session.commit()
   except:        
        error = True
        db.session.rollback()
        print(sys.exc_info())
   finally:
        db.session.close()           
        if  error == True:
            abort(400)
        else:            
            return jsonify(body)

@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.all())


#always include this at the bottom of your code (port 3000 is only necessary in workspaces)

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=3000)