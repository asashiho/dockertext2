from flask import Flask, render_template
import os,random

app = Flask(__name__)

# comfigmap.yaml
project_id = os.environ.get('PROJECT_ID')

# secrets.yaml
secret_id = os.environ.get('SECRET_ID')
secret_key = os.environ.get('SECRET_KEY')

images = [
    "docker-machine-01.jpg",
    "docker-machine-02.jpg",
    "docker-machine-03.jpg",
    "docker-machine-04.jpg",
    "docker-machine-05.jpg"
]

@app.route('/')
def index():
    image_path = "/static/images/" + random.choice(images)
    return render_template('index.html', image_path=image_path, pid=project_id, id=secret_id, key=secret_key)

# Main
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))
    print(project_id)
    try:
        app.run(host="0.0.0.0", port=port, debug=True)
    except Exception as ex:
        print(ex)