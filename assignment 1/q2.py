
def frequency(string):
    output = {}
    for i in string:
        keys = output.keys()
        if i in keys:
            output[i] += 1
        else:
            output[i] = 1
    return output
print(frequency('google.com'))