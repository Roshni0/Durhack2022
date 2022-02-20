import csv
# importing the requests library
import requests
rows = []
post_results = []

with open("output.csv", 'r') as file:
    csvreader = csv.reader(file)
    headers = next(csvreader)

    for row in csvreader:
        new_house = House(price=row[1], location=row[2], num_bedrooms=int(row[7]), website=row[3], sqrft=500)
        post_results.append(new_house)

# data to be sent to api
data = {
        # 'api_dev_key':API_KEY,
		# 'api_option':'paste',
		# 'api_paste_code':source_code,
		# 'api_paste_format':'python'
        'lists':post_results
        }

# sending post request and saving response as response object
res = requests.post('http://localhost:5000/tests/endpoint', data=data)