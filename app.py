from flask import Flask

app = Flask(__name__)

@app.route('/')

#1 - morphological analysis (based on Lab 01, using farasa , i )
def morphological_analysis(text):

# run the app
if __name__ == '__main__':

    app.run()