import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the student marks from the marks.json file
def load_marks():
    with open('q-vercel-python.json', 'r') as f:
        return json.load(f)

@app.route("/api", methods=["GET"])
def get_marks():
    # Get the list of names from the query parameters
    names = request.args.getlist('name')
    
    # Load marks from the JSON file
    student_marks = load_marks()
    
    # Get the marks for the requested students
    marks = [student_marks.get(name, "Student not found") for name in names]
    
    return jsonify({"marks": marks})

if __name__ == "__main__":
    app.run(debug=True)
