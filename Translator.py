import mlconjug

class Translator:
    def __init__(self):
        global conjugator
        global tenseKeyDict
        global subjectKeysDict
        conjugator = mlconjug.Conjugator(language='es')
        tenseKeyDict = {'preterite' : ['Indicativo', 'Indicativo pretérito perfecto simple'], 'present' : ['Indicativo', 'Indicativo presente'], 'imperfect' : ['Indicativo', 'Indicativo pretérito imperfecto'], 'subjunctive' : ['Subjuntivo', 'Subjuntivo presente']}
        subjectKeysDict = {'yo':'1s', 'tu':'2s', 'el/ella':'3s', 'nosotros':'1p', 'ellos/ellas':'3p'}

    def conjugate(self, verb, tense, subject):
        conjugatedVerb = conjugator.conjugate(verb).conjug_info
        key1 = tenseKeyDict[tense][0]
        key2 = tenseKeyDict[tense][1]
        key3 = subjectKeysDict[subject]
        return conjugatedVerb[key1][key2][key3]