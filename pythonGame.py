import pymysql.cursors
import random as rd

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '209213',
    db = 'english',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def verbsConjugation():

    while True:

        question = rd.randint(1, 2)

        a = rd.randint(0, len(verbs) - 1)
        print(f'a: {a}')
        verbDictionary = verbs[a]
        columns = ['base form', 'past simple', 'past participle', 'meaning']
        columnNumber = rd.randint(0, 3)

        verb = verbDictionary['verb']
        pastSimple = verbDictionary['pastSimple']
        pastParticiple = verbDictionary['partParticiple']
        meaning = verbDictionary['meaning']

        # if question == 1:
        print(f'What is the past simple and past participle of \'{verb.upper()}\'?')
        ps = input('Past Simple:     ')
        pt = input('Past Participle: ')

        rightPS = False
        rightPT = False

        if ps == pastSimple:
            rightPS = True
        if pt == pastParticiple:
            rightPT = True

        if rightPS and rightPT:
            print(f'{bcolors.OKGREEN}RIGHT!')
            print('='*20)
            print(f'gabarito: {pastSimple}')
            print(f'resposta: {ps}')
        else:
            print(f'\033[91mWRONG!')
            print(f'Past Simple:     {pastSimple}')
            print(f'Past Participle: {pastParticiple}')
            print('='*20)

        Continue = input('Do you want to continue? [y/n] ')

        if Continue == 'n':
            break

        # if question == 2:
        #     print(f'What is the verb that such past participle is \'{pastParticiple.upper()}\'?')
        #     v = input('Verb: ')

        #     rightV = False


try:                                                   # ----- LISTA DE VERBOS
    with conexao.cursor() as cursor:
        cursor.execute('select * from verbs;')
        verbs = cursor.fetchall()
except:
    print('Erro ao conectar ao banco de dados dos pedidos')


verbsConjugation()