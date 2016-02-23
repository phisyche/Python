def mysum(*numbers): # * operator allows the function to recieve any no. of arguments
    output = 0
    for number in numbers:
        output += number
    return output
