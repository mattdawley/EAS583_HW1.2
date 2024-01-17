import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"

	pinata_api_url = "https://api.pinata.cloud/pinning/pinFileToIPFS"

	headers = {
		"pinata_api_key": "bf5730d128884333e83b",
		"pinata_secret_api_key": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiI5NzdkNjQ0Ny01NzRlLTRlMDgtYTg5Zi05MjZjOTkyZjdiMDUiLCJlbWFpbCI6ImRhd2xleUBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicGluX3BvbGljeSI6eyJyZWdpb25zIjpbeyJpZCI6IkZSQTEiLCJkZXNpcmVkUmVwbGljYXRpb25Db3VudCI6MX0seyJpZCI6Ik5ZQzEiLCJkZXNpcmVkUmVwbGljYXRpb25Db3VudCI6MX1dLCJ2ZXJzaW9uIjoxfSwibWZhX2VuYWJsZWQiOmZhbHNlLCJzdGF0dXMiOiJBQ1RJVkUifSwiYXV0aGVudGljYXRpb25UeXBlIjoic2NvcGVkS2V5Iiwic2NvcGVkS2V5S2V5IjoiYmY1NzMwZDEyODg4NDMzM2U4M2IiLCJzY29wZWRLZXlTZWNyZXQiOiIwNjI0NTA5MjUxZDYwNTYzYWNlY2I0NzExZjUzM2VkOWFhODc5OTQxNmY4ZDY5YzZiMTdjZDQ3MmIwMDc0OGVhIiwiaWF0IjoxNzA1NDUxODYzfQ.u-rfF1aPkaoqtbcgjNbkmqxwj6xhYlHj9llFTaYAJKc",
	}

	# Open and read the file
	file_path = "data.json"
	with open(file_path, "w") as file:
		json.dump(data, file)

		files = {"file": (file_path, file)}
		response = requests.post(pinata_api_url, headers=headers, files=files)

		# Check if the request was successful (status code 200)
		if response.status_code == 200:
			cid = response.json()["IpfsHash"]
			print("File pinned successfully!")
			print("IPFS Hash:", response.json()["IpfsHash"])
		else:
			print("Failed to pin file. Status code:", response.status_code)
			print("Response:", response.text)

	return cid

	test_dict = {"a":1, "b":2, "c":3}
	pin_to_ipfs(test_dict)

def get_from_ipfs(cid,content_type="json"):
	pass
	#assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	

	#assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	#return data
