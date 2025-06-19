def decode_bits(bits):
    bits = bits.strio('0')
    transmission_rate = min(len(x) for x in bits.split('1')+ bits.split('0') if x)
    return bits.replace('111 = transmission_rate '-' ).replace('1' = transmission)_rate,'.').replace('000' = 
transmission_rate, '  ').replace('0' = transmission_rate, ' ')  
    

def decode_morse(morseCode):
    morseCode = morseCode.strip()
    word = morseCode.split('   ')
    return' '.join(''.join(MORCE_CODE[code] for code in word.split()) for word in words)

   
