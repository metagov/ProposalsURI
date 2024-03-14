from flask import Flask, request, jsonify
import requests
import os 

app = Flask(__name__)


boardroomApiConfig = {
    "1": "https://api.boardroom.info/v1/protocols",
    "10": "https://api.boardroom.info/v1/protocols",
}


BOARDROOM_KEY = os.getenv('BOARDROOM_KEY')

def api_request(path, method="GET", data=None):
    headers = {"Content-Type": "application/json"}
    if method == "POST":
        response = requests.post(path, json=data, headers=headers)
    else:
        response = requests.get(path, headers=headers)
    return response.json()


@app.route('/', methods=['GET'])
def api_documentation():
    documentation = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>DAOstar Proposals URI API Documentation</title>
    </head>
    <body>
        <h1> API Documentation</h1>
        <h2>Endpoints</h2>
        <ul>
            <li>
                <strong>GET /api/v1/boardroom/proposals/{network}/{id}</strong> - Retrieve proposals based on the network and id.
            </li>
        </ul>
        <h2>Parameters</h2>
        <p>
            <strong>network</strong> - The blockchain network id.<br>
            <strong>id</strong> - The unique identifier for the entity within the network.
        </p>
        <h2>Query Parameters</h2>
        <p>
            <strong>cursor</strong> - Optional. A cursor for pagination.
        </p>
        <p> Example: https://proposalsuri.onrender.com/api/v1/boardroom/proposals/10/ens?cursor=<cursor> </p>
    </body>
    </html>
    """
    return documentation

@app.route('/api/v1/boardroom/proposals/<network>/<id>', methods=['GET'])
def get_proposals(network, id):
    path = boardroomApiConfig.get(network)
    if not path:
        return jsonify(message="Missing config for network"), 400
    
    cursor = request.args.get('cursor')
    query_path = f"{path}/{id}/proposals?limit=50&key={BOARDROOM_KEY}"
    if cursor:
        query_path += f"&cursor={cursor}"

    res = api_request(query_path)

    if not res.get('data'):
        return jsonify(message="DAO not found"), 404
    
    proposals = res['data']
    next_cursor = res.get('nextCursor', '')
    
    proposals_formatted = [{
        "type": "proposal",
        "id": a['id'],
        "name": a['title'],
        "status": a['currentState'],
    } for a in proposals]

    transformed = {
        "proposals": proposals_formatted,
        "@context": "http://www.daostar.org/schemas",
        "type": "DAO",
        "name": id,
        "nextCursor": next_cursor,
    }

    return jsonify(transformed)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

