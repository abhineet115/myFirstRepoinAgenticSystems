# completed assignment
import json

data ={
  "id": "req_123",
  "status": "success",
  "result": {
    "text": "Hello world",
    "confidence": 0.98
  }
}

json_data = data
print("Request ID: ",json_data["id"])
print("Status: ",json_data["status"])
print("Text: ",json_data["result"]["text"])
print("Confidence: ",json_data["result"]["confidence"])

if json_data["result"]["confidence"] < 0.9:
  print("Warning: Low confidence level")


with open("response.json", "w") as f:
  json.dump(json_data, f)
