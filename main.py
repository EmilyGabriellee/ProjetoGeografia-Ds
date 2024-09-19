from pymongo import MongoClient
from datetime import date
import os
import time
import random 

id_random = random.randint(0,9999999)

client = MongoClient('localhost',27017)#conectar banco de dados

db = client.segurancaplus

seguranca = db.registro
while True:
    os.system('color 6')
    os.system('cls')
    
    print('sistema de boletim de ocorrencia\n\n [1]registrar ocorrencia\n [2]conferir registro\n [3]deletar registro')
    entrar = int(input(' '))
    #registrar ocorrencia
    os.system('cls')
    os.system('color f')
    if entrar == 1:
        
        name = str(input('Digite o seu nome: '))
        sobrenome = str(input('Digite sobrenome: '))
        cpf = str(input('Insira cpf: '))
        descricao = str(input('O que aconteceu:\n'))
        hj = str(date.today())
        os.system('cls')
        print('processando')
        time.sleep(1)
        os.system('cls')
        print('processando.')
        time.sleep(1)
        os.system('cls')
        print('processando..')
        time.sleep(1)
        os.system('cls')
        print('processando...')
        time.sleep(1)
        os.system('cls')
        print('Ocorrencia registrada')
        
        seguranca.insert_one({
            '_id': id_random,
            'nome': name,
            'sobrenome': sobrenome,
            'CPF': cpf,
            'data_registro':hj ,
            'descricao': descricao  
        })
        input(' ')
        os.system('cls')
    #conferir registros
    elif entrar == 2:
        os.system('color 1')
        print('buscar por:\n [1]nome\n [2]data de registro\n [3]data da ocorrencia\n [4]mostrar todos os registros')
        busca = int(input(' '))
        if busca == 1:
            nome_busca =  str(input('insira o nome\n'))
            os.system('cls')
            print('buscando')
            time.sleep(1)
            os.system('cls')
            print('buscando.')
            time.sleep(1)
            os.system('cls')
            print('buscando..')
            time.sleep(1)
            os.system('cls')
            print('buscando...')
            time.sleep(1)
            os.system('cls')
            print('resultados:\n')
            
            for i in seguranca.find({"nome":nome_busca}):
                print(i)
            input(' ')
                
        elif busca == 2:
            print('insira a data de registro(siga esse modelo:ano-mês-dia')
            registro = str(input(' '))
            os.system('cls')
            print('buscando')
            time.sleep(1)
            os.system('cls')
            print('buscando.')
            time.sleep(1)
            os.system('cls')
            print('buscando..')
            time.sleep(1)
            os.system('cls')
            print('buscando...')
            time.sleep(1)
            os.system('cls')
            print('resultados:\n')
            for i in seguranca.find({'data_registro':registro}):
                print(i)
            input(' ')
        else:
            os.system('cls')
            print('buscando')
            time.sleep(1)
            os.system('cls')
            print('buscando.')
            time.sleep(1)
            os.system('cls')
            print('buscando..')
            time.sleep(1)
            os.system('cls')
            print('buscando...')
            time.sleep(1)
            os.system('cls')
            print('resultados:\n')
            for i in seguranca.find({}):
                print(i)
            input(' ')
        os.system('cls')
    elif entrar ==3:
        deletar = int(input('insira ID do registro'))
        for i in seguranca.find({'_id': deletar}):
            print(i)
        confirmar = int(input('deseja deletar registro?\n [1]sim\n [2]não'))
        if confirmar == 1:
            seguranca.delete_one({"_id": deletar})
        else:
            print('voltando')
    else:
        break
    
