import secrets
from timeit import default_timer
from string import ascii_letters, digits, ascii_lowercase, hexdigits, punctuation, printable
from rarfile import RarFile

used_passwords = set() # Blank database to store used passwords
used_passwords.clear()


# Script config here
characters_to_use = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
input_file_path = "/input/file/path"  # Which file to brute-force
output_file_path = "/output/file/path"  # Where extracted content should be outputted
password_length = 1  # Set the minimal/start length to the password
tries_count = 0
max_tries = (len(characters_to_use)**password_length)


def generate_random_password(password_length):
    return ''.join(secrets.choice(characters_to_use) for _ in range(password_length))


def recalc_max_tries():
    global max_tries
    max_tries = (len(characters_to_use)**password_length)


def attempt_to_unzip(word):
    try:
        with RarFile(input_file_path, mode='r') as rar_file:
            rar_file.setpassword(word)
            rar_file.extractall(path=output_file_path)
        return True
    except:
        return False


if __name__ == "__main__":
    start_time = default_timer()

    print("Generating Password")
    while True:
        if tries_count == max_tries:
            print("INCREASING PASSWORD RANGE")
            password_length += 1
            used_passwords.clear()

        word = generate_random_password(password_length)

        if word not in used_passwords:
            print(f"\"{word}\"")
            used_passwords.add(word)

            if attempt_to_unzip(word) is True:
                stop_time = default_timer()
                print(f"THIS OPERATION HAS TAKEN: {round(stop_time - start_time)} seconds")
                print(f"DISCOVERED AFTER {tries_count} TRIES")
                print(f"THE PASSWORD IS: {word}")
                break
            else:
                tries_count += 1

