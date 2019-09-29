from flask import Flask, flash, redirect, render_template, request, session, abort
import QuizEngine
import random
app = Flask(__name__)

@app.route("/")
def question():
    q, a = QuizEngine.newQuestion()
    question = {'word': q[0], 'tense': q[1], 'subject': q[2], 'answer': a}
    debugnum = random.randint(0, 1000000)
    return render_template('homepage.html', question=question, debug=debugnum)

if __name__ == "__main__":
    app.run(debug=True, use_debugger=False, use_reloader=False, passthrough_errors=True)
