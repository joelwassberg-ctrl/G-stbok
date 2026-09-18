from flask import Flask, redirect, request, render_template_string
import os, json, datetime

app = Flask(__name__)

FILE_PATH = 'media.json'


def read_data():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            data = json.load(file)
    else:
        data = []
    return data

@app.route('/', methods=['GET'])
def index():
    return render_template_string(open('templates/media.html').read(), media=read_data(), ensure_ascii=False)


@app.route('/text-channel', methods=['POST'])
def write():
    media = read_data()
    media.append({
        'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'name': request.form.get('name', ''),
        'topic': request.form.get('topic', ''),
        'message': request.form.get('message', '')
    })
    with open(FILE_PATH, 'w') as file:
        json.dump(media, file, indent=2)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')