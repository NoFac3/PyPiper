from nltk.stem import WordNetLemmatizer as WNL
import spacy
nlp = spacy.load('en_core_web_lg')

def Tokenize(word):
    token = nlp(word)
    return token

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

def WordVector(word):
    token = Tokenize(word)
    if token.has_vector==True:
        return token.vector
    else:
        return 0

def WordNorm(word):
    token = Tokenize(word)
    return token.vector_norm
