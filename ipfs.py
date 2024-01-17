import requests
import json

# secret

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"

	pinata_api_url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
	headers = {
		"pinata_api_key": "4e8b2b5c83d672a0f9af",
		"pinata_secret_api_key": "3b3a7b65f0d95d6efa153fc46578f966241c71f1f9f43c7d199c6d4d0d10c82a",
	}

	json_data = json.dumps(data)
	payload = { "pinataContent": json_data }

	response = requests.post(pinata_api_url, json=payload, headers=headers)

	# Check if the request was successful (status code 200)
	if response.status_code == 200:
		cid = response.json()["IpfsHash"]
	else:
		cid = "na"

	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	pinata_gateway_url = "https://green-kind-shark-845.mypinata.cloud/ipfs/"+cid
	headers = {
		"pinata_api_key": "4e8b2b5c83d672a0f9af",
		"pinata_secret_api_key": "3b3a7b65f0d95d6efa153fc46578f966241c71f1f9f43c7d199c6d4d0d10c82a",
	}
	response = requests.get(pinata_gateway_url, headers=headers)
	data = response.json()
	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data

# get_from_ipfs("QmeaKXvbjjnttzu4ttAzjDQ2wHR97uCX84LyyAyLMtLagm")
