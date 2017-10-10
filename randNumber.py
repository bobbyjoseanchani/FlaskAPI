from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
import random

app = FlaskAPI(__name__)



@app.route("/", methods=['GET'])
def random_number():
	"""
	Get a random number.
	"""
	
	# Read arguments
	my_type = request.args.get('type', None)
	my_length = request.args.get('length', None)
	my_random_numbers = []
	success = True
	
	# Validate arguments and get random numbers from range
	if my_type is None:	
		success = False
	elif my_length is None: 
		success = False
	else:
		my_length = int(my_length)
		if my_type == 'uint8': 
			my_random_numbers = random.sample(xrange(255), my_length)
		elif my_type == 'uint16':
			my_random_numbers = random.sample(xrange(65535), my_length)
		elif my_type == 'hex16':
			# Not implementing in the interest of time
			my_random_numbers = random.sample(xrange(65535), my_length) 
		else:
			success = False
		
	if not success:
		return {
			"success" : False
		}
	else:	
		return {
			'type': my_type,
			'length': my_length,
			'data': my_random_numbers,
			'success': True
		}


if __name__ == "__main__":
	app.run(debug=True)