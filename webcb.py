from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)


df = pd.read_excel('samplecb.xlsx')

@app.route('/')
def home():
    return render_template('WebChatBot.html', **locals())

@app.route('/get_answer', methods=['POST'])
def get_answer():
    question = request.form['question'].lower().strip() 

    try: 
        answer = df[df['question'] == question]['answer'].values[0]  
    except: 
        answer = '5 chú báo chưa dạy tui câu ni!!'
    
    return render_template('WebChatBot.html', question=question, answer=answer)

if __name__ == '__main__':
    app.run()
