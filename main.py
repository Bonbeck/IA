import spacy
from spacy import displacy
#from lib2to3.pgen2 import token
#from nltk.tokenize import RegexpTokenizer

texto = "Pode ser que o Matheus digite qualquer uma frase em Maringa."
#tokenizer = RegexpTokenizer(r"[A-z]\w*")
#tokens = tokenizer.tokenize(texto)
#
#print(tokens)

nlp = spacy.load("pt_core_news_sm")

interpretador = nlp(texto)
print(type(interpretador))

for token in interpretador:
    print(token, token.idx, token.shape_, token.tag_)
#for entidade in interpretador.ents:
#    print(entidade.text, entidade.label_)