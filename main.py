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
