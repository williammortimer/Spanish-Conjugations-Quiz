import ConjugationTrainer

def newQuestion():
    quizNumber = 1
    cjt = ConjugationTrainer.ConjugationTrainer(quizNumber)
    question = cjt.generateQuestion()
    q, a = question['question'], question['answer']
    return q, a


