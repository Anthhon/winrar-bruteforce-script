import rarfile  # Allow the script to interact with winrar files
from timeit import default_timer    # This module provides a simple way to time small bits of Python code.
from random import choice   # This module implements pseudo-random number generators for various distributions.
from string import ascii_letters # You can use ascii letters, ascii_lowercase or ascii_uppercase to define wha type of passwords you wanna try


# Blank database for used passwords
triesDbs = list()
# Clear the database just for sure
triesDbs.clear()


# Set here the file path to extract
def filePath():
    return "./where/is/the/file.rar"


# Set here path where the file should be extracted
def finalPath():
    return "./extraction/path"


def generate_string(passwordLength):
    # This function create random strings custom sized using string module
    # The "ascii_letters" refeer to upper and lowercase passwords
    # You can choose into:
    # ascii_letters -> 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # ascii_lowercase -> 'abcdefghijklmnopqrstuvwxyz'
    # ascii_uppercase -> 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # digits -> '0123456789'
    # hexdigits -> '0123456789abcdefABCDEF'
    # punctuation -> !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    # printable -> All ASCII characters considered printable. A combination of, digits, ascii_letters, punctuation and whitespace
    return (''.join((choice(ascii_letters) for x in range(passwordLength))))


def check_word_in_Database(word):
    if word not in triesDbs:
        triesDbs.append(word)
        return False
    else:
        print("___ALREADY USED PASSWORD___")
        return True


def try_password(word):
    try:
        with rarfile.RarFile(filePath(), mode='r') as archive:
            archive.setpassword(word)
            archive.extractall(path=finalPath())
        return True
    except:
        return False


# If the program cannot found the password in actual range, this funcion will increase the password range.
def passwordOutOfRange(counter, maxRange):
    return bool(counter == maxRange)


def unzip_suceeded():
    stop = default_timer()
    print(f"THIS OPERATION HAS TAKEN: {round(stop - start)} seconds")
    print(f"DISCOVERED AFTER {counter} TRIES")
    print(f"THE PASSWORD IS: {word}")
    quit()


def unzipFailed():
    stop = default_timer()
    print(f"THIS OPERATION HAS TAKEN: {stop - start} seconds")
    print(f"TRIED {counter} COMBINATIONS")
    quit()


start = default_timer() # Starts timer
counter = 0 # Counts how much times the code iterated
passwordLength = 1  # Set the minimal length to the password


while True:

    maxRange = ((26**passwordLength)*(passwordLength*passwordLength))

    '''
    This piece of code puts a limit in your password range if you want

    if passwordLength == 3:
        print("O código possui algum erro")
        quit()
    '''

    if passwordOutOfRange(counter, maxRange) is True:
        print("INCREASING PASSWORD RANGE")
        passwordLength += 1
        triesDbs.clear()

    word = generate_string(passwordLength)
    print("Generating Password")
    print(f"Trying: {word}")

    if check_word_in_Database(word) is True:
        continue
    else:
        print(f"Trying: {word}")
        if try_password(word) is True:
            unzip_suceeded()
        else:
            counter += 1
