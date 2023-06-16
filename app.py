from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "shop rana",
        'items': [
            {
                "name": "chair",
                "price": 10
            }
        ]
    },
]

@app.get("/stores")
def get_stores():
    return { "stores": stores}


@app.post("/store")
def create_store():
    request_data = request.get_json()
    tmp_new_store = {"name": request_data["name"], "items": []}
    stores.append(tmp_new_store)

    return { "stores": stores} , 201


@app.post("/store/<string:name>/item")
def create_item(name):
    store_name = name
    request_data = request.get_json()

    for store_detail in stores:
        if store_detail["name"] == name:
            print("===============")
            # store_details = stores["name"]
            store_detail["items"].append(request_data)
            return { "stores": stores} , 201
        
    return {"message": "store not found"}, 404
