from time import *
import random as r


def mistake(par, user):
    err = 0
    for i in range(len(par)):
        try:
            if par[i] != user[i]:
                err += 1
        except UnicodeError:
            err += 1
    return err


def speed_type(i_time, e_time, u_input):
    time_delay = e_time - i_time
    r_time = round(time_delay, 2)
    speed = len(u_input) / r_time
    return round(speed)


if __name__ == '__main__':
    while True:
        ck = input("Ready to test : yes/no : ")
        if ck == 'yes':
            test = ["A paragraph is a self contained unit of discourse"
                    " in writing dealing with a particular point or idea.",
                    "paragraph consists of one or more sentences. "
                    "paragraphs are usually an expected part of formal writing",
                    "A paragraph used to organize longer prose."]

            test1 = r.choice(test)
            print(" ****** Typing Speed ****** ")
            print(test1)
            print()
            time_1 = time()
            userInput = input(" Enter : ")
            time_2 = time()

            print('Typing Speed :', speed_type(time_1, time_2, userInput), "word/s")
            print('Typing Error :', mistake(test1, userInput), "word/s")
        elif ck == 'no':
            print("Thank you")
            break
        else:
            print("Enter valid Input")
