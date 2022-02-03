from flask import Flask, request, abort
import json
import requests
app = Flask(__name__)

@app.route('/', methods=['POST'])
def welcom():
	return 'A Simple webhook'


@app.route('/webhook', methods=['POST'])
def webhook():
	if request.method == 'POST':
		print("received data",request.json)
		json_string = json.dumps(request.json)
		data = json_string
		if 'hello' in data:
			URL = "https://google.com"
			r = requests.get(url = URL)
			print('Request sent')
		else:
			print ('not there')
			return 'success', 200
		return 'OK'
	else:
		abort(400)
		print("failed")


if __name__ == '__main__':
	app.run(debug=True)