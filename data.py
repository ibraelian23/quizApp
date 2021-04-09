import requests
parameters = {
    "amount": 10,
    "category": 31,
    "difficulty": "easy",
    "type": "boolean"
}

data = requests.get(url="https://opentdb.com/api.php",params=parameters).json()
question_data = data["results"]