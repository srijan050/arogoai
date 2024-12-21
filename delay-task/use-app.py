import requests

url = "http://127.0.0.1:5000/predict"
payload = {
    "Origin": "Kolkata",
    "Destination": "Chennai",
    "Vehicle Type": "Trailer",
    "Weather Conditions": "Clear",
    "Traffic Conditions": "Moderate"
}

response = requests.post(url, json=payload)
print(response.json())
