from flask import Flask , jsonify , request

app = Flask(__name__)

# initialise to do list
items = [
    {"id":1,"name":Item1,"Description":"this is item 1"},
    {"id":2,"name":Item2,"Description":"this is item 2"},
]

@app.route('/')
def home():
    return "Sample todo list app"

@app.route('/items',methods=['GET'])
def get_item():
    return jsonify(items)
# get request
@app.route('/items/<int:item_id>',methods=['GET'])
def item(item_id):
    item = next((item for item in items if item["id"] == item_id),None)
    if item is None:
        return jsonify({"error":"item not found"})
    return jsonify(item)

#post request
@app.route('/items'.Method['POST'])
def create_item():
    if not request.json or not "name" in request.json:
        return jsonify({"error":"item not found"})
    new = {
        "id" : items[-1]["id"] +1 if items else 1,
        "name" : request.json['name']
    }


if __name__=="__main__":
    app.run(debug=True)
