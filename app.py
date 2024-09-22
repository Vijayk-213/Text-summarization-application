from flask import Flask, render_template, request
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import nltk
nltk.download('punkt_tab')
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = ""
    if request.method == 'POST':
        text = request.form['text']
        num_sentences = int(request.form['num_sentences'])
        
        # Create a parser for the plaintext
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        
        # Create the summarizer
        summarizer = LsaSummarizer(Stemmer("english"))
        summarizer.stop_words = get_stop_words("english")
        
        # Summarize the text
        summary = ' '.join([str(sentence) for sentence in summarizer(parser.document, num_sentences)])
    
    return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)