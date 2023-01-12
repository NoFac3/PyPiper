from nltk.stem import WordNetLemmatizer as WNL
import spacy
nlp = spacy.load('en_core_web_lg')

def Tokenize(word):
    token = nlp(word)
    return token

def token_vector(word):
    token = Tokenize(word)
    if token.has_vector==True:
        return token.vector
    else:
        return 0

def token_vector_norm(word):
    token = Tokenize(word)
    return token.vector_norm

def Similarity(words):
    token1, token2 = Tokenize(words)
    return token1.similarity(token2)

def SimilarLoop(words):
    S=[]
    for k in range(len(words)-1):
        for j in range(1,len(words)):
            s = words[k]+" "+words[j]
            S.append(Similarity(s))
    return S

def WordNorm(word):
    token = nlp(word)
    norm = token.vector_norm
    return norm

def RootWord(word):
    lem = WNL()
    w = lem.lemmatize("".join(word))
    return w

from numpy import log as ln

def entropy(dist):
    su = 0
    for p in dist:
        r = p/sum(dist)
        if r==0:
            su+=0
        else:
            su+= -r*(ln(r))
    return su/ln(2)
