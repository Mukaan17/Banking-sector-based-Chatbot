from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

try:
	os.remove("db.sqlite3")
	print("Old database removed. Training new database")
except:
	print('No database found. Creating new database.')

english_bot = ChatBot('Steve')
trainer = ListTrainer(english_bot)
for file in os.listdir('data'):
        print('Training using '+file)
        convData = open('data/' + file).readlines()
        trainer.train(convData)
        print("Training completed for "+file)
    

