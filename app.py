from deeppavlov import build_model, configs
model_qa_ml = build_model(configs.squad.squad_bert_multilingual_freezed_emb, download=True)  

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
content = 'Hi, I am ananthaprakash. This is a general content. You have to provide a content to make the chatbot to answer for your questions. Good Luck'

@app.route("/")
def hello():
    return render_template('chat.html')

@app.route("/ask", methods=['POST'])
def ask():
  message = request.form['messageText'].encode('utf-8').lower().decode()
  #kernel now ready for use
  while True:
    if message == "quit":
      #exit()
      bot_response = "Bye Bye. Ended Successfully.\n LOL just kidding :). I am running in server. So, I won't stop :D"
    elif message == "hi":
      bot_response = "Hello, Please start asking the questions"
    elif message.find("!content")!=-1:
      #Write in notepad
      context = message
      with open("./content.txt","w") as cont:
        cont.write(message)
      bot_response = "Content Successfully Overwritten"
    elif (message.find("created")!=-1 and message.find("you")!=-1) or message.find("ananthaprakash")!=-1:
      bot_response = "I was created by Ananthaprakash"
    else:
      bot_response = str(model_qa_ml([context],[message])      )
      return jsonify({'status':'OK','answer':bot_response})
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug=True)
