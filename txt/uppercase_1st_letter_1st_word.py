with open("Vocab.txt", "r") as f:
    lines = f.readlines()

    for line in lines:
        list_of_string = list(line)

        # Replace the first letter of the first word in a line to uppercase
        if line[0].isalpha():
            list_of_string[0] = line[0].upper()
            line = ''.join(list_of_string)
        
        # Replace the first letter of the first word after "=" in a line to uppercase
        index_of_meaning_symbol = line.find('=')
        index_of_alphabet_after_meaning_symbol = index_of_meaning_symbol + 2

        if index_of_meaning_symbol > 0 and line[index_of_alphabet_after_meaning_symbol].isalpha():
            list_of_string[index_of_alphabet_after_meaning_symbol] = line[index_of_alphabet_after_meaning_symbol].upper()
            line = ''.join(list_of_string)
        
        with open("Vocab_edited.txt", "a") as o:
            o.write(line)
