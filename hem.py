def hamming_encode(data):

    r = 0
    while 2**r < len(data) + r + 1:
        r += 1
    

    encoded_data = [None] * (len(data) + r)
    j = 0
    for i in range(1, len(encoded_data) + 1):
        if i & (i - 1) == 0:
            encoded_data[i - 1] = 0
        else:
            encoded_data[i - 1] = int(data[j])
            j += 1
    

    for i in range(r):
        pos = 2**i - 1
        sum_bits = 0
        for j in range(pos, len(encoded_data), 2 * pos + 2):
            sum_bits += sum(encoded_data[j:j+pos+1])
        encoded_data[pos] = sum_bits % 2
    
    return encoded_data

def hamming_decode(encoded_data):
    r = 0
    while 2**r < len(encoded_data):
        r += 1
    
    encoded_data = list(map(int, encoded_data))
    error_bit = 0

    for i in range(r):
        pos = 2**i - 1
        sum_bits = 0
        for j in range(pos, len(encoded_data), 2 * pos + 2):
            sum_bits += sum(encoded_data[j:j+pos+1])
        if (sum_bits % 2) != 0:
            error_bit += pos + 1
            #print(error_bit)
    

    if error_bit > 0:
        encoded_data[error_bit - 1] = 1 - encoded_data[error_bit - 1]
    

    decoded_data = []
    for i in range(1, len(encoded_data) + 1):
        if i & (i - 1) != 0:
            decoded_data.append(encoded_data[i - 1])
    
    return decoded_data


print(hamming_encode('1011'))
print(hamming_decode('0110011'))