#Неверные пароли

wrongpasswords = []

def checkpoint():
    # Неверные пароли
    global wrongpasswords, run_of_questions
    # noinspection PyBroadException
    check = input('Do you want to restore the checkpoint?(y/n)\n').lower()
    global run
    if check == 'y':
        print('Recovery')
        # noinspection PyBroadException
        try:
            with open('password, length, n.txt', 'rb') as f:
                # password_0 = password, length, n   null password - begin password, length of this password, count
                password_0 = pickle.load(f)
            run_of_questions = False
            print('File #1 restored')
        except:
            print('\nFailed to open system file #1')
            password_0 = None
            run_of_questions = True

        try:
            with open('wrongpasswords.txt', 'rb') as f:
                words = pickle.load(f)
            for word in words:
                wrongpasswords.append(word)
            run = True
            run_of_questions = False
            print('File #2 restored')
        except FileNotFoundError:
            password_0 = None
            run = False
            run_of_questions = True
            print('\nFailed to open system file #2')
        print('Done!')
    elif check == 'n':
        password_0 = None
        run = False
        run_of_questions = True
    else:
        print('A nonexistent value was entered. Checkpoint is not restored')
        password_0 = None
        run = False
        run_of_questions = True

    return wrongpasswords, password_0, run, run_of_questions

def main():
    global alphabet, wrongpasswords, run, run_of_questions
    wrongpasswords, password_0, run, run_of_questions = checkpoint()
    if run_of_questions == False:
        try:
            with open('variable.txt', 'r') as f:
                password_generator = f.read(1)
                login_generator = f.read()
                password_generator = int(password_generator)
                login_generator = int(login_generator)
        except FileNotFoundError:
            print('Save file error')
            main()
    elif run_of_questions == True:
        while True:
            loginner = input('Enter the number of the login generator:\n1) Goal\n2) Popular usernames\n')
            # noinspection PyBroadException
            try:
                login_generator = int(loginner)
            except:
                print('Set popular logins')
                login_generator = 2
            finally:
                break

        while True:
            passworder = input(
                'Enter the password generator number:\n1) Bruteforce\n2) Popular passwords\n3) Random password\n')
            # noinspection PyBroadException
            try:
                password_generator = int(passworder)
            except:
                print('Set popular passwords')
                password_generator = 2
            finally:
                break
    else:
        print('It can\'t be that important X0')

    new_liters = input('Add Russian letters to the list of characters?(y/n)\n').lower()
    if new_liters == 'y':
        alphabet += dop_alphabet
        print('Added')
    elif new_liters == 'n':
        print('Not added')
    else:
        print('A nonexistent value was entered. Not added')

    if login_generator == 1:
        if password_generator == 1:
            # 1 1
            Variables.login_list_with_bruteforce(alphabet, wrongpasswords, password_0, run, run_of_questions)
        elif password_generator == 2:
            # 1 2
            Variables.login_list_with_popular_passwords(wrongpasswords)
        elif password_generator == 3:
            # 1 3
            Variables.login_list_with_random_choice(alphabet, wrongpasswords, password_0, run, run_of_questions)
    elif login_generator == 2:
        if password_generator == 1:
            # 2 1
            Variables.popular_logins_with_bruteforce(alphabet, wrongpasswords, password_0, run, run_of_questions)
        elif password_generator == 2:
            # 2 2
            Variables.popular_logins_with_popular_passwords()
        elif password_generator == 3:
            # 2 3
            Variables.popular_logins_with_random_choice(alphabet, wrongpasswords, password_0, run, run_of_questions)
    else:
        print('You entered a nonexistent value. Try again')


main()