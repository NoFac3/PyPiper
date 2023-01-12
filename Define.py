import nltk
nltk.download("wordnet")
nltk.download('omw-1.4')
from nltk.corpus import wordnet
from py_thesaurus import Thesaurus
from nltk.stem import WordNetLemmatizer as WNL
import Memory as M

def wordTag(self,user_input):
        words = nltk.word_tokenize(user_input)
        tag = nltk.pos_tag(words)
        return tag

def RootWord(word):
    lem = WNL()
    w = lem.lemmatize("".join(word))
    return w

def getDef(w):
        word = w
        try:
                w = RootWord(word)
                wtype = wordnet.synsets(w)
                wType = wtype.pos()
                wordType = w+"."+wType+".01"
                defin = wordnet.synset(wordType).definition()
        except:
                print(f"Error [{word}<--->{w}]")
                wtype = ""
                defin = ""
        if defin == "":
                data,keys = M.ReadJson("dictionary.json")
                for k in keys:
                    if k==w:
                        defin = data[k]
                if defin == "":
                    for k in keys:
                        if k==word:
                            defin = data[k]
        return defin

def getSynonym(w):
        synonyms=[]
        for syn in wordnet.synsets(w):
            for lm in syn.lemmas():
                synonyms.append(lm.name())
        if len(synonyms)==0:
            syn = "NONE"
        else:
            for word in synonyms:
                if w in synonyms:
                    synonyms.remove(word)
            syn=[]
            [syn.append(x) for x in synonyms if x not in syn]
        return syn

def getAntonym(w):
        antonyms = []
        for syn in wordnet.synsets(w):
            for lm in syn.lemmas():
                if lm.antonyms():
                    antonyms.append(lm.antonyms()[0].name())
        if len(antonyms)==0:
            ant = "NONE"
        else:
            for word in antonyms:
                if w in antonyms:
                    antonyms.remove(word)
            ant=[]
            [ant.append(x) for x in antonyms if x not in ant]
        return ant

def getThesarus(w):
        thesaurus = Thesaurus(w)
        defin = thesaurus.get_definition()
        syn = thesaurus.get_synonym()
        synV = thesaurus.get_synonym(pos='verb')
        synAdj = thesaurus.get_synonym(pos='adj')
        ant = thesaurus.get_antonym()
        return defin,syn,synV,synAdj,ant
