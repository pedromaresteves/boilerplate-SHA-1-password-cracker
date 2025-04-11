import hashlib

def crack_sha1_hash(hash, use_salts = False):
    read_top_passwords = open('top-10000-passwords.txt', 'r')
    top_passwords_arr = read_top_passwords.read().split('\n')
    read_salts = open('known-salts.txt', 'r')
    salts = read_salts.read().split('\n')
    for word in top_passwords_arr:
        if use_salts:
            for salt in salts:
                prepended_hashed_word = hash_word(salt + word)
                apended_hashed_word = hash_word(word + salt)
                if prepended_hashed_word == hash:
                    return word
                if apended_hashed_word == hash:
                    return word
        else:
            hashed_word = hash_word(word)
            if hashed_word == hash:
                return word
    return "PASSWORD NOT IN DATABASE"

def hash_word(word):
    sha1 = hashlib.sha1()
    sha1.update(word.encode())
    hashed_hex = sha1.hexdigest()
    return hashed_hex

