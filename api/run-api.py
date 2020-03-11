from flask import Flask, request, send_file, Markup, Response
import spacy
from spacy import displacy
#from io import BytesIO
import os

nlp = spacy.load('es_core_news_sm')

app = Flask(__name__)

@app.route('/')
def entry():
    return """<a href="https://github.com/SergioGomis/NLP_in_Social_Media">About this project</a>"""

@app.route('/text/<texto_entrada>')
def texto2img(texto_entrada):
    
    doc = nlp(texto_entrada)
    svg = displacy.render(doc, style="dep", jupyter=False)

    return Response(svg, mimetype='image/svg+xml')

app.run("0.0.0.0", os.getenv("PORT"), debug=True)

