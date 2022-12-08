from rarfile import RarFile  # https://pypi.org/project/rarfile/
from timeit import default_timer    # https://docs.python.org/3/library/timeit.html
from random import choice   # https://docs.python.org/3/library/random.html?highlight=random#module-random
from string import ascii_letters, digits # https://docs.python.org/3/library/string.html?highlight=string#module-string

# Blank database to store used passwords
tries_db = list()
tries_db.clear()



def filePath():
    return "path"    # Set here the file path to bruteforce
def finalPath():
    return "path"          # Set here path where the file should be extracted


def pass_out_of_range(counter, maxRange):
    return bool(counter == maxRange)

def generate_password(passwordLength):
    # The "ascii_letters" refeer to upper and lowercase passwords
    # You can choose into:
    # ascii_letters -> 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # ascii_lowercase -> 'abcdefghijklmnopqrstuvwxyz'
    # ascii_uppercase -> 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # digits -> '0123456789'
    # hexdigits -> '0123456789abcdefABCDEF'
    # punctuation -> !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    # printable -> All ASCII characters considered printable. A combination of, digits, ascii_letters, punctuation and whitespace
    return (''.join((choice(digits) for x in range(passwordLength))))

def check_word_in_Database(word):
    if word not in tries_db:
        tries_db.append(word)
        return False
    else:
        print("___ALREADY USED PASSWORD___")
        return True

def try_password(word):
    try:
        with RarFile(filePath(), mode='r') as rar_file:
            rar_file.setpassword(word)
            rar_file.extractall(path=finalPath())
        return True
    except:
        return False



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
counter = 0 # Counts how much passwords were used
passwordLength = 3  # Set the minimal/start length to the password


while True:

    # Define the password max tries range
    maxRange = ((26**passwordLength)*(passwordLength*passwordLength))

    if pass_out_of_range(counter, maxRange) is True:
        print("INCREASING PASSWORD RANGE")
        passwordLength += 1
        tries_db.clear()    # Clear the database to avoid clustering

    word = generate_password(passwordLength)
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
