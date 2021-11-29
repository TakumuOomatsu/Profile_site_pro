from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def top():
  return render_template('index.html')

if __name__ == "__app__":
  port = int(os.getenv("PORT,5000"))
  app.run(host="0.0.0.0", port=port)