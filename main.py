
from nltk.chat.util import Chat, reflections  # use pip install nltk

pairs = [
    ['(hi|hello|hey)', [ 'Hey!, My name is PrabhuBot. Im here to help you :)']],
    ['My name is (.*)', ['Hello! %1, How can I help you today?']],
    ['Thank you', ['Anytime!']],
    ['(.*) your name ?', ['My name is PrabhuBot. I will connect you to customer representative if I dont have the answer to your question']],
    ['(.*) executive ?', ['Sure! Connecting you with one of our free customer representative']],
    ['(.*) my order ?', ['Checking the status of your order...']]

]
#print(reflections)
#dummy_ref ={'hi':'bye'}

chat = Chat(pairs, reflections)
#print(chat._substitute('hi there!'))
chat.converse()