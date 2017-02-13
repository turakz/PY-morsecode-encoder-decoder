import sys
from collections import OrderedDict

#populate our encoder/decoder dictionaries
def fillDicts(encoder, decoder):

    #get rules from file
    fInput = file('morsecode.txt')

    #split each line intio a key, value pair--ignore \n
    for line in fInput:
        if line.strip():
            key, value = line.strip().split()
            encoder[key] = value
            decoder[value] = key



def parse(encoder, decoder):

    pText = str(raw_input('>> '))
    cText = pText

    #are we encoding or decoding?
    if pText[0].isalpha():
        #encoding
        cText = encode(encoder, pText)

    else:
        #decoding
        pText = decode(decoder, cText)

    return pText, cText


def encode(encoder, cText):
   
    pText = ""
    for word in cText:
        if word == " ":
            continue
        pText = pText + encoder[word.upper()]
        pText = pText + " "

    return pText



def decode(decoder, pText):

    cText = ""
    for word in pText.split():
        if word == "/":
            cText = cText + " "
            continue
        cText = cText + decoder[word]

    return cText


#initialize our key, value containers
encoder = OrderedDict()
decoder = OrderedDict()

#fill them
fillDicts(encoder, decoder)

print 'Welcome to Morse-code Encoder/Decoder!\n'
print 'Select input method (bad input terminates program):\n'
print 'user\n', 'exit\n',

inputMethod = str(raw_input('\n> '))

while (inputMethod == 'user'):

    if inputMethod == 'exit':
        break
    ptext, ctext = parse(encoder, decoder)
    print '\nplain-text: ', ptext
    print 'cypher-text: ', ctext, '\n'
    print 'user\n', 'exit\n'
    inputMethod = str(raw_input('> '))


print 'Have a nice day!'
