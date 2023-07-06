use std::env;
use std::collections::HashSet;
use rand::Rng;

pub const ASCII_LETTERS:&str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
pub const ASCII_UPPERCASE:&str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
pub const ASCII_LOWERCASE:&str = "abcdefghijklmnopqrstuvwxyz";
pub const DIGITS:&str = "0123456789";
pub const HEXDIGITS:&str = "0123456789abcdefABCDEF";
pub const PUNCTUATION:&str = "#$%&'()*+,-./:;<=>?@[\\]^_`{|}~";

fn generate_password(password_length: usize, used_passwords: &HashSet<String>) -> String {
    let mut password: String;
    loop {
        password = (0..password_length)
            .map(|_| {
                let index = rand::thread_rng().gen_range(0..ASCII_LETTERS.len());
                ASCII_LETTERS.chars().nth(index).unwrap()
            })
            .collect();

        if !used_passwords.contains(&password) {
            break;
        }
    }
    password
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let _filepath: &String = args.get(1).unwrap(); 

    // TODO: Parse and check arguments

    let mut used_passwords: HashSet<String> = HashSet::new();
    let mut password_length: usize = args.get(2).unwrap().parse::<usize>().unwrap();
    let mut tries_counter: usize = 0;
    let mut tries_max: usize = ASCII_LETTERS.len().pow(password_length as u32);

    println!("[+] GENERATING PASSWORDS");
    loop {
        let new_password: String = generate_password(password_length, &used_passwords);
        print!("\r └ {}", new_password);

        used_passwords.insert(new_password.clone());
        tries_counter += 1;

        // Updates counter when needed
        if tries_counter >= tries_max {
            tries_max = ASCII_LETTERS.len().pow(password_length as u32);
            password_length += 1;
        }

        // Advise when password has been found
        if new_password == "hard" {
            println!("\n   └ PASSWORD FOUND");
            break;
        }
    }
}
