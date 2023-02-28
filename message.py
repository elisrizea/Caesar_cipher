# ************************************************************************************************************ #
# Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of     #
# the simplest and most widely known encryption techniques. It is a type of substitution cipher in which       #
# each letter in the plain text is replaced by a letter some fixed number of positions down the alphabet. For  #
# example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named  #
# after Julius Caesar, who used it in his private correspondence.                                              #
# ************************************************************************************************************ #

import pyperclip

# Save colors in constants to decorate the console output
GREEN = '\033[92m'
RED = '\033[91m'
END = '\033[0m'


# ******************************** class Cipher ******************************************
# Use alphabet tuple to replace every char with another that have index+step
class Cipher:
    # Add chars to alphabet tuple for better results
    alphabet = (
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'A', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l' 'm', 'n', 'o', 'p', 'q', 'r',
        's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', '.', ',',
        '!', '?', '_', '-', '=', '+', '&', '*', '%', '$', '@', '£', '#', '\'', '"', '<', '>', '%')

    def __init__(self, step, ):
        if step <= 0 or step > len(self.alphabet) - 1:
            # Unreachable line left her for class safety
            self.step = len(self.alphabet) // 2
            print(
                f'Chosen step must be between {GREEN}0{END} and {GREEN}{len(self.alphabet) - 1}{END}.'
                f' Your chosen step is out of range and will be automatically set at {GREEN}{step}{END}\n')
        else:
            self.step = step

    # Getter alphabet size
    def alphabet_size(self):
        return len(self.alphabet) - 1

    # *********** Encrypt method ***************
    def encrypt(self, c):
        if c in self.alphabet:
            index = self.alphabet.index(c) + self.step
            if index <= len(self.alphabet) - 1:
                return self.alphabet[index]
            else:
                return self.alphabet[index - len(self.alphabet)]
        else:
            return c

    # *********** Decrypt method ***************
    def decrypt(self, c):
        if c in self.alphabet:
            index = self.alphabet.index(c) - self.step
            if index >= 0:
                return self.alphabet[index]
            else:
                return self.alphabet[len(self.alphabet) + index]
        else:
            return c


# *************************** def do_operation(step, operation, message)**************************
# Return encrypted/decrypted message
# You can apply multiple crypt and decrypt for better results
# (keep in mind this algorithm is basic)
def do_operation(step, operation, message):
    op = Cipher(step)
    if operation == 'e':
        return "".join(map(op.encrypt, message))
    else:
        return "".join(map(op.decrypt, message))


# ************** Main menu *********
# Initialise main menu vars
info = Cipher(1)
message, operation, step = '', '', 0
do_continue, do_clip = '', ''

while True:
    # ********** Request user input *************
    #  operation, step and message
    if operation == '':
        operation = input(f'Do you want to {GREEN}(e){END}ncrypt or {GREEN}(d){END}ecrypt?\n>').strip().lower()
    if len(operation) > 1:
        operation = operation[0]
    if operation not in ('e', 'd'):
        print('\nPlease enter d to decrypt or e to encrypt')
        operation = input(f'Do you want to {GREEN}(e){END}ncrypt or {GREEN}(d){END}ecrypt?\n>').strip().lower()
        continue
    try:
        step = int(step)
        if step <= 1 or step > info.alphabet_size():
            step = input(f'Please enter the key {GREEN}(1 to {info.alphabet_size()}){END} to use.\n>')
            continue
    except ValueError:
        print(f'{RED}Please enter a number{END}')
        step = input(f'Please enter the key {GREEN}(1 to {info.alphabet_size()}){END} to use.\n>')
        continue
    if message == '' and operation == 'e':
        message = input(
            f'Enter the message to {GREEN}encrypt{END} or press {GREEN}(p){END}paste to past your clipboard content\n> ')
        if message in ('p', 'P', 'Paste', 'PASTE', 'paste'):
            message = pyperclip.paste()
            print(f'Your message is:\n{GREEN}{message}{END}')
        continue
    elif message == '' and operation == 'd':
        message = input(
            f'Enter the message to {GREEN}decrypt.{END} or press {GREEN}(p){END}paste to past your clipboard content\n> ')
        if message in ('p', 'P', 'Paste', 'PASTE', 'paste'):
            message = pyperclip.paste()
            print(f'Your message is:\n {GREEN}{message}{END}')
        continue
    elif do_clip == '':

        # Print the result (if "y" is press, when requested, save the result to clipboard)
        result = do_operation(step, operation, message)
        print(f'\nYour result is: \n{GREEN}{result}{END}')
        do_clip = input(
            f'\nIf you want to save your resulted message to clipboard press {GREEN}(c){END}opy,'
            f' to skip press any other key\n>').strip().lower()
        if do_clip in ('c', 'copy'):
            pyperclip.copy(result)
            print(f'{GREEN}Your result has been copied to your clipboard{END}')

        # If "y" is press reset vars and start another operation
        # any other key exit program
        if do_continue == '':
            do_continue = input(
                f'\nTo do another operation pres {GREEN}(y){END}es,'
                f' to exit program press any other key\n>').strip().lower()
            if len(do_continue) > 1:
                do_continue = do_continue[0]
                continue
            elif do_continue == 'y':
                operation, message, do_continue, do_clip, step = '', '', '', '', 0
                continue
            else:
                quit()
