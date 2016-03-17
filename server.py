from flask import Flask, render_template, request
import shlex
import subprocess as sp
import requests
import traceback
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/css')
def css():
    return app.send_static_file('style.css')

@app.route('/js/<jsfile>')
def js(jsfile):
    return app.send_static_file(jsfile)

@app.route('/image/<img>')
def image(img):
    return app.send_static_file(img)

@app.route('/VQA', methods=['POST', 'GET'])
def VQA():
	try:
		if request.method == 'POST':
			try:
				url = request.form['image_url']
				question = request.form['question']
				imfile = request.files['image_file']
				path = '/home/ubuntu/neural-vqa/test'
				# path = '/home/deepali/test'

				if url:
					extension = os.path.splitext(url)[-1]
					f_name = path + extension
					response = requests.get(url)
					with open(f_name, 'wb') as f:
						f.write(response.content)
				elif imfile:
					extension = os.path.splitext(imfile.filename)[1]
					ff_name = path + extension
					imfile.save(ff_name)

				command = "/home/ubuntu/torch/install/bin/th predict.lua -checkpoint_file data/vqa_epoch23.26_0.4610_cpu.t7 -input_image_path test" + extension + " -question '" + question + "'"
				args = shlex.split(command)
				
				try:
					p = sp.check_output(args, cwd='/home/ubuntu/neural-vqa/')
					answer = p.split('\n')[-2][:-1]
				except Exception as e:
					answer = 'err: ' + str(traceback.format_exc())
				
				result = {'answer': answer}
				return json.dumps(result)

			except Exception as e:
				return json.dumps({'error': 'err: ' + str(e)})
	except Exception as e:
		return json.dumps({'error': 'err: ' + str(e)})

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)
