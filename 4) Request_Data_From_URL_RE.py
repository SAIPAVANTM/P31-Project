import requests
import re

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
response = requests.get(url)
data = response.text
first_names = re.findall(r'\b([A-Za-z]+)\b,', data)
print(first_names)
