import requests

response = requests.get('http://artii.herokuapp.com/make?text=asd&font=acrobatic')
print(response.text)