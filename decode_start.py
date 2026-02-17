alphabet = " abcdefghijklmnopqrstuvwxyz"
vowel = "aeiou"
message = ""
with open("secret.txt") as f:
    for line in f:
         # instead of print, you should start decoding
        # count vowels
        # index the alfabet via the vowels count to get the letter
        # collect all letters

        num_vowels = 0
        for v in vowel:
            num_vowels = num_vowels + line.count(v)
        letter = alphabet[num_vowels]
        message = message + letter
    print(message)