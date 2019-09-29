import Translator
import random

class ConjugationTrainer:
    def __init__(self, quiz):
        global myTranslator
        global wordSetIndex
        global wordSets
        global tenseSets
        global subjectSet
        wordSetIndex = quiz
        wordSets = {
            1: ['hablar', 'vivir', 'estar', 'ser', 'dar', 'hacer', 'decir', 'dormir', 'escribir', 'saber' , 'salir', 'ver', 'trabajar', 'oír', 'comer'],
            2: ['querer', 'ver', 'socializar', 'poner', 'morir', 'hacer', 'decir', 'escribir', 'conocer', 'cambiar' , 'abrir', 'descubrir', 'romper', 'educar', 'desempeñar']
                    }
        tenseSets = {1: ['present', 'preterite', 'imperfect', 'subjunctive'],
                     2: ['ppi, pps']}
        subjectSet = ['yo', 'tu', 'el/ella', 'nosotros', 'ellos/ellas']
        myTranslator = Translator.Translator()

    #conjugate method takes a verb, tense:[present, preterite, imperfect, subjunctive, ppi, pps], and subject:[yo, tu, el/ella, nosotros, ellos/ellas]
    def generateQuestion(self):
        word = random.choice(wordSets[wordSetIndex])
        tense = random.choice(tenseSets[wordSetIndex])
        subject = random.choice(subjectSet)
        conjugation = myTranslator.conjugate(word, tense, subject)
        return {'question': [word, tense, subject], 'answer': conjugation}