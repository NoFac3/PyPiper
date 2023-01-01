import nltk
nltk.download("wordnet")
nltk.download('omw-1.4')
from nltk.corpus import wordnet
from py_thesaurus import Thesaurus

class Define(object):
    def wordTag(self,user_input):
        words = nltk.word_tokenize(user_input)
        tag = nltk.pos_tag(words)
        return tag
        #print("\n   TAGS: ",tag,"----->",tag[0],"\n")

    def getDef(self,w,tag):
        if w =="you" or w=="we":
            return
        else:
            wtype = wordnet.synsets(w)[0]
            wType = wtype.pos()
            wordType = w+"."+wType+".01"
            defin = wordnet.synset(wordType).definition()
            x=""
            ex=""
            if len(wordnet.synset(wordType).examples())==0:
                return "NONE"
            else:
                ex = wordnet.synset(wordType).examples()
                x = len(ex)
            return w,defin,x,ex


    def getSyn(self,w):
        synonyms=[]
        for syn in wordnet.synsets(w):
            for lm in syn.lemmas():
                synonyms.append(lm.name())
        if len(synonyms)==0:
            return "NONE"
        else:
            for word in synonyms:
                if w in synonyms:
                    synonyms.remove(word)
            syn=[]
            [syn.append(x) for x in synonyms if x not in syn]
            return len(syn),syn

    def getAnt(self,w):
        antonyms = []
        for syn in wordnet.synsets(w):
            for lm in syn.lemmas():
                if lm.antonyms():
                    antonyms.append(lm.antonyms()[0].name())
        if len(antonyms)==0:
            return "NONE"
        else:
            for word in antonyms:
                if w in antonyms:
                    antonyms.remove(word)
            ant=[]
            [ant.append(x) for x in antonyms if x not in ant]
            return len(ant),ant
          
    # word net seems to have an issue with the word "you" 
    def getYou(self,w):
        defs = {"1":"the pronoun of the second person singular or plural, used of the person or persons being addressed, in the nominative or objective case:",
                "2":"one; anyone; people in general:",
                "3":"(used in apposition with the subject of a sentence, \n\t\t    sometimes repeated for emphasis following the subject):",
                "4":"Informal. (used in place of the pronoun your before a gerund):"}
        ex = {
            "1":"You are the highest bidder. It is you who are to blame.\n\t\t    We can't help you. This package came for you.\n\t\t    Did she give you the book?",
            "2":"a tiny animal you can't even see.",
            "3": "You children pay attention. You rascal, you!",
            "4": "There's no sense in you getting upset."}

        return defs, ex
