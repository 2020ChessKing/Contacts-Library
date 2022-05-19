from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [
    {
        "id" : 1,
        "name" : u"John Doe",
        "number" : u"92213452132",
        "done" : False,
    },
    {
        "id" : 2,
        "name" : u"Jane Doe",
        "number" : u"23345768022",
        "done" : False,
    }
]

@app.route("/")
def intro():
    return "Welcome to the Contacts Library!"

@app.route("/add-contact", methods=["POST"])
def add_contact():
    if not request.json:
        return jsonify({
            "status" : "error",
            "message" : "Please provide the data!!"
        }, 400)

    contact = {
        "id" : contacts[-1]['id'] + 1,
        "name" : request.json["Name"],
        "number" : request.json.get("number", ""),
        "done" : False
    }

    contacts.append(contact)

    return jsonify({
        "status" : "success",
        "message" : "Task added successfully!"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : contacts
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)