import random as rd
from verbs import verbs
import numpy as np
from adjectives import adjectives as adjlist

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

    i = 0

    while True:

        question = rd.randint(1, 5)

        a = rd.randint(0, len(verbs) - 1)
      
        verbDictionary = verbs[a]

        verb = verbDictionary['verb']
        pastSimple = verbDictionary['pastSimple']
        pastParticiple = verbDictionary['pastParticiple']
        meaning = verbDictionary['meaning']

        if question == 1:
            print(f'{bcolors.ENDC}What is the {bcolors.UNDERLINE}past simple{bcolors.ENDC} and {bcolors.UNDERLINE}past participle{bcolors.ENDC} of \'{verb.upper()}\'?')
            ps = input(f'{bcolors.ENDC}Past Simple:     ')
            pt = input(f'{bcolors.ENDC}Past Participle: ')

            rightPS = False
            rightPT = False

            if ps == pastSimple:
                rightPS = True
            if pt == pastParticiple:
                rightPT = True

            if rightPS and rightPT:
                print(f'{bcolors.OKGREEN}RIGHT!')
                i += 1
            else:
                print(f'{bcolors.FAIL}WRONG!')
                print(f'{bcolors.ENDC}Past Simple:     {bcolors.WARNING}{ pastSimple}')
                print(f'{bcolors.ENDC}Past Participle: {bcolors.WARNING}{pastParticiple}')
                i = 0

        # NEXT TYPE OF QUESTION

        if question == 2:
            print(f'{bcolors.ENDC}What is the {bcolors.UNDERLINE}verb{bcolors.ENDC} which past participle is \'{pastParticiple.upper()}\'?')
            v = input('Verb: ')

            rightV = False

            if v == verb:
                rightV = True

            if rightV:
                print(f'{bcolors.OKGREEN}RIGHT!')
                print(f'{bcolors.ENDC}The meaning of {verb} is: {bcolors.WARNING}{meaning}')
                i += 1
            else:
                print(f'{bcolors.FAIL}WRONG!')
                print(f'{bcolors.ENDC}The verb is {verb}')
                i = 0

        if question == 3:
            print(f'{bcolors.ENDC}What is the {bcolors.UNDERLINE}verb{bcolors.ENDC} which past simple is \'{pastSimple.upper()}\'?')
            v = input('Verb: ')

            rightV = False

            if v == verb:
                rightV = True

            if rightV:
                print(f'{bcolors.OKGREEN}RIGHT!')
                print(f'{bcolors.ENDC}The meaning of {verb} is: {bcolors.WARNING}{meaning}')
                i += 1
            else:
                print(f'{bcolors.FAIL}WRONG!')
                print(f'{bcolors.ENDC}The verb is {verb}')
                i = 0

        if question == 4:
            print(f'{bcolors.ENDC}What is the {bcolors.UNDERLINE}past simple form{bcolors.ENDC} which past participle is \'{pastParticiple.upper()}\'?')
            v = input('Verb: ')

            rightV = False

            if v == pastSimple:
                rightV = True

            if rightV:
                print(f'{bcolors.OKGREEN}RIGHT!')
                print(f'{bcolors.ENDC}The meaning of {verb} is: {bcolors.WARNING}{meaning}')
                i += 1
            else:
                print(f'{bcolors.FAIL}WRONG!')
                print(f'{bcolors.ENDC}The past simple is {pastSimple}')
                i = 0

        if question == 5:
            print(f'{bcolors.ENDC}What is the {bcolors.UNDERLINE}past pasticiple form{bcolors.ENDC} which past simple is \'{pastSimple.upper()}\'?')
            v = input('Verb: ')

            rightV = False

            if v == pastParticiple:
                rightV = True

            if rightV:
                print(f'{bcolors.OKGREEN}RIGHT!')
                print(f'{bcolors.ENDC}The meaning of {verb} is: {bcolors.WARNING}{meaning}')
                i += 1
            else:
                print(f'{bcolors.FAIL}WRONG!')
                print(f'{bcolors.ENDC}The past participle is {pastParticiple}')
                i = 0

        print(f'{bcolors.ENDC}|'+f'{bcolors.OKGREEN}#'*i+f'{bcolors.ENDC}#'*(50-i)+'|')

        print(f'{bcolors.OKBLUE}='*20)

        if i == 50:
            print(f'{bcolors.OKCYAN}CONGRATULATIONS! YOU WON THE GAME!')
            break


def adjectives():

    pontuaction = 0

    while True:

        options = ['a', 'b', 'c', 'd', 'e']
        answerLetter = rd.choice(options)
        answerNumber = options.index(answerLetter)

        a = rd.randint(0, len(adjlist) - 1)
        adjectiveDictionary = adjlist[a]

        adjective = adjectiveDictionary['adjective']
        meaning = adjectiveDictionary['meaning']
        example = adjectiveDictionary['example']

        adjectivesindex = []

        print(f'{bcolors.OKBLUE}='*20)
        print(f'{bcolors.ENDC}Select the adjective which means {bcolors.UNDERLINE}\'{meaning}\'{bcolors.ENDC}:')

        i = 0

        while i < 5:

            random = rd.randint(0, len(adjlist) - 1)
            if random != a and random not in adjectivesindex:
                adjectivesindex.append(random)        
                i += 1

        adjectivesindex[answerNumber] = a

        for i in range(len(options)):

            index = adjectivesindex[i]
            adj = adjlist[index]
            print(options[i] + ')', adj['adjective'])

        while True:

            answer = input('answer: ')

            if answer not in options:
                pass    
            elif options.index(answer) == answerNumber:
                print(f'{bcolors.OKGREEN}RIGHT!')
                pontuaction += 1
                break
            else:
                print(f'{bcolors.FAIL}WRONG!')
                print(f'{bcolors.ENDC}The adjective is {adjective}')
                pontuaction = 0
                break
        
        print(f'{bcolors.ENDC}EXAMPLE: {bcolors.WARNING}{example}')
    
        print(f'{bcolors.ENDC}|'+f'{bcolors.OKGREEN}#'*pontuaction+f'{bcolors.ENDC}#'*(50-pontuaction)+'|')

        if pontuaction == 50:
            print(f'{bcolors.OKCYAN}CONGRATULATIONS! YOU WON THE GAME!')
            break

# verbsConjugation()
# adjectives()
