def compress(data):
    dictionary = {chr(i): i for i in range(256)}
    next_code = 256
    result = []
    current_code = ""
    for symbol in data:
        current_code += symbol
        if current_code not in dictionary:
            dictionary[current_code] = next_code
            next_code += 1
            result.append(dictionary[current_code[:-1]])
            current_code = symbol
    result.append(dictionary[current_code])
    return result
def decompress(compressed_data):
    dictionary = {i: chr(i) for i in range(256)}
    next_code = 256
    result = [compressed_data[0]]
    w = chr(compressed_data[0])
    for k in compressed_data[1:]:
        if k in dictionary:
            entry = dictionary[k]
        elif k == next_code:
            entry = w + w[0]
        else:
            raise ValueError("Bad compressed k: %d" % k)
        result.append(entry)
        dictionary[next_code] = w + entry[0]
        next_code += 1
        w = entry
    return ''.join(result)
if __name__ == "__main__":
    original_data = "TOBEORNOTTOBEORTOBEORNOT"
    compressed_data = compress(original_data)
    decompressed_data = decompress(compressed_data)
    
    print("Original Data: ", original_data)
    print("Compressed Data: ", compressed_data)
    print("Decompressed Data: ", decompressed_data)

