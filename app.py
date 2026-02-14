from flask import Flask, render_template, request, jsonify
import networkx as nx

app = Flask(__name__)

# Create mall graph
mall_map = nx.Graph()

# Nodes (locations)
locations = [
    "Entrance",
    "Lift",
    "Food Court",
    "Nike Store",
    "Zara",
    "Restroom",
    "Exit"
]

mall_map.add_nodes_from(locations)

# Connections (paths)
mall_map.add_edges_from([
    ("Entrance", "Lift", {"weight": 2}),
    ("Entrance", "Nike Store", {"weight": 4}),
    ("Lift", "Food Court", {"weight": 3}),
    ("Nike Store", "Zara", {"weight": 2}),
    ("Zara", "Food Court", {"weight": 4}),
    ("Food Court", "Restroom", {"weight": 2}),
    ("Restroom", "Exit", {"weight": 3})
])

@app.route("/")
def home():
    return render_template("index.html", locations=locations)

@app.route("/navigate", methods=["POST"])
def navigate():
    data = request.json
    start = data["start"]
    end = data["end"]

    try:
        path = nx.dijkstra_path(mall_map, start, end)
        return jsonify({"path": path})
    except:
        return jsonify({"error": "Path not found"})

if __name__ == "__main__":
    app.run(debug=True, host="10.228.217.131")
