"""import tokenizer
from flask import Flask, request, render_template

from tokenizer import text_tokenizer

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_list,  processed_text = text_tokenizer(text)
    return processed_text

"""
from flask import Flask, request, render_template,jsonify

from tokenizer import text_tokenizer



app = Flask(__name__)


@app.route('/', methods=['POST'])
def my_form_post():
    text1 = request.args.get('text1',type=str)
    processed_list,  processed_text, reduced  = text_tokenizer(text1)
    result = {
        "output_text": processed_text,
        "output_list" : processed_list,
        "reduced_by": reduced
    }
    #result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

    
if __name__ == '__main__':
    app.run(threaded = True)