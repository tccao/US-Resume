
def decode(message_file):
    f = None
    try: 
        f = open(message_file, 'r') 
    except OSError:
        print("----Error Opening File----")
    with f:
        #Initialize variables
        decoded_sentence = ''
        number_subsets = []
        number_to_word = dict()

        #Create a dictionary map from number to word and list of number subsets
        for line in f:
            number,word = line.split()
            number_to_word[number] = word
            number_subsets.append(number)
        
        #Create a list of number subsets that form a staircase
        number_subsets = create_staircase(number_subsets)
        
        #Check if the number of subsets is enough to form a staircase
        if number_subsets == False:
            print("""Cannot decode the message because the 
                  number of subsets is not enough to form a staircase""")
            return
        
        # Form decoded_sentence from the number_subsets
        for subset in number_subsets:
            last_number = subset[-1]
            decoded_sentence += number_to_word[last_number] + ' '
        
        return(decoded_sentence)

def create_staircase(number_subsets):
    step = 1
    subsets = []
    while len(number_subsets) != 0:
        if len(number_subsets) >= step:
            subsets.append(number_subsets[0:step])
            number_subsets = number_subsets[step:]
            step += 1
        else:
            return False
    return subsets

"""
The function decode(message_file) requires message_file as the URL to 
the coding_qual_input.txt file. Reading the message_file is wrapped around
a try-except-with block to ensure errors are handled properly and file is
closed after used. Then, we create a dictionary map from number to word
and a list of number from message_file. This list of number is used to create
a number_subsets staircase through function create_staircase(number_subsets).
The decode(.) function would halt and return NULL if create_staircase(.)
fails to create the staircase from the given number_subsets. Finally, we 
extracted the last word from the end of each subset in the staircase by mapping
the number to its corresponding word in the number_to_word dictionary and append
it to the decoded_sentence. The decoded_sentence is returned as the output of the
decode(.) function.
"""
message_file = './coding_qual_input.txt'
print(decode(message_file))