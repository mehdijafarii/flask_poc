from flask import Flask

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

@app.get("/store")
def get_stores():
    return { "stores": stores}