import nltk
nltk.download("wordnet")
nltk.download('omw-1.4')
from nltk.corpus import wordnet
from py_thesaurus import Thesaurus
from nltk.stem import WordNetLemmatizer

class Define(object):
    def wordTag(self,user_input):
        words = nltk.word_tokenize(user_input)
        tag = nltk.pos_tag(words)
        return tag

    def getDef(self,w):
        word = w
        if w =="you":
            defin = {"1":"the pronoun of the second person singular or plural, used of the person or persons being addressed, in the nominative or objective case:","2":"one; anyone; people in general:","3":"(used in apposition with the subject of a sentence, \n\t\t    sometimes repeated for emphasis following the subject):","4":"Informal. (used in place of the pronoun your before a gerund):"}
        else:
            try:
                lemmatizer = WordNetLemmatizer()
                w = lemmatizer.lemmatize(w,pos=wtype)
                wtype = wordnet.synsets(w)
                wType = wtype.pos()
                wordType = w+"."+wType+".01"
                defin = wordnet.synset(wordType).definition()
            except:
                print(f"Error [{word}<--->{w}]")
                wtype = ""
                defin = ""
        return defin

    def getSynonym(self,w):
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

    def getAntonym(self,w):
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

    def getThesarus(self,w):
        thesaurus = Thesaurus(w)
        defin = thesaurus.get_definition()
        syn = thesaurus.get_synonym()
        synV = thesaurus.get_synonym(pos='verb')
        synAdj = thesaurus.get_synonym(pos='adj')
        ant = thesaurus.get_antonym()
        return defin,syn,synV,synAdj,ant
