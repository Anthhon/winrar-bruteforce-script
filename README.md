# PyWinrarBruteForce

This code tries to brute-force a password-protected RAR file by generating random passwords of increasing length and attempting to extract the file using each one until the correct password is found or the maximum number of tries is reached.

The 'RarFile' class from the 'rarfile' library is used to open the RAR file in read-only mode, and the 'setpassword' method is used to set the password to be used to extract the file. The 'extractall' method is then called to extract the contents of the file to a specified directory. If the password is incorrect, an exception will be raised, and the except block will be executed.

The 'generate_random_password' function uses the 'secrets' module to generate a random string of the specified length using the 'choice' function from the random module, which selects a 'random' element from a given iterable.

The 'is_password_used' function checks if the generated password has already been tried by checking if it is in the 'used_passwords' list. If it has, the function returns True, and the loop will continue to the next iteration without attempting to extract the file. If the password has not been used, it is added to the 'used_passwords' list and the function returns False.

The 'is_max_tries_reached' function checks if the maximum number of tries has been reached by comparing the current number of tries to the specified maximum. If the maximum number of tries has been reached, the function returns True, and the loop will increase the password length and clear the 'used_passwords' list before continuing.

The 'unzip_success' and 'unzip_failure' functions are called when the file is successfully extracted or the maximum number of tries is reached, respectively. These functions print the elapsed time and the number of tries, and then exit the program.
