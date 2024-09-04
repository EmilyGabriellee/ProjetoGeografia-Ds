from questionario import Resposta,db
import os

db.connect()

db.create_tables([Resposta])
os.system('color a')

nome = str(input('Qual o seu nome?\n'))
assaltos = int(input('Houve algum assalto recentemente?Se sim,quantos?\n'))
parente = str(input('Você possui algum conhecido que foi assaltado recentemente?(y/n)\n'))
viatura = int(input('Há um bom numero de viaturas em ronda?\n'))
base = int(input('Existe alguma base policial 24H por perto?Se sim,quantas?\n'))
nota = 0


if assaltos > 5 or parente == 'y':
    nota+=3
if viatura < 10 and base < 2:
    nota+=6
elif viatura < 10 and base > 2:
    nota+=3
elif viatura > 10 and base < 2:
    nota+=3    
else:
    print('pipoca')
    
