def number_needed(a, b):
    #Create a array of 26 elements all set to 0 (26 letter of the alphabet)
    frequency_of_letters = [0] * 26
    letter_to_remove = 0
    list_a = list(a)
    list_b = list(b)
    
    # We loop the list_a and obtain the ASCII value of the letter.plus 1 in the equivalent index of the current letter
    for letter_a in list_a:
        frequency_of_letters[ord(letter_a) - ord('a')]+=1
        
    # We loop the list_b and obtain the ASCII value of the letter.plus 1 in the equivalent index of the current letter
    for letter_a in list_b:
        frequency_of_letters[ord(letter_a) - ord('a')]-=1

    #We loop the list of frequency_of_letters and obtain the abosule value (-1 = 1 and +1 = 1)
    for e in frequency_of_letters:
        letter_to_remove += abs(e)
    
    return letter_to_remove
    
        

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
