class Eval():
    def __init__(self, expression_string = None):
        '''break up this expression into a list'''
        self.expression_string = expression_string
        self.expression_list = []

        if expression_string is not None:
            self.expression_list = self.expression_string_to_list(expression_string)

    def __repr__(self):
        return self.expression_string

    def expression_string_to_list(self, expression_string):
        '''given an expression in the form of a string
        return the expression in the form of a list'''
        symbols = set([*"^*/+-"]) # these are the symbols we want to look out for
        expression_list = [] # create an array to store the split up expression
        for char in expression_string: # iterate through each char in the expression string
            if char in symbols: # check if the char is in our set of symbols
                expression_list.append(char) # if so add the symbol to our list
            elif char.isdigit(): # otherwise check if our char is a digit
                # check if the last index of our array is also an int
                if len(expression_list) > 0 and type(expression_list[-1]) == int:
                    # if so add the char (string) to that int and convert them to an int
                    expression_list[-1] = int(str(expression_list[-1]) + char)
                else:
                    # otherwise just add the char in int form
                    expression_list.append(int(char))
        return expression_list # once we traverse the string return what we've collected

    def find(self, arr, item, item2 = None):
        '''find the first instance of up to 2 items in an array and return its index'''
        for i, char in enumerate(arr):
            if char == item or char == item2:
                return i
    
    def find_num_of_occurances(self, arr, item, item2 = None):
        '''given an array and an item, return the number of times that item is found in the array'''
        incrementor = 0
        for char in arr:
            if char == item or char == item2:
                incrementor += 1
        return incrementor

    def exponents(self, part):
        '''return the inputted array with the first exponents evaluated'''
        i = self.find(part, "^") # find the index of the first instance of ^
        result = part[i - 1] ** part[i + 1] # evaluate whats around it
        part.pop(i) # remove the evaluated vals
        part.pop(i) # remove the evaluated vals
        part[i - 1] = result # input the result in place
        return part # return the manipulated array

    def multiplication_or_division(self, part):
        '''return the inputted array with the first multiplication or division evaluated'''
        i = self.find(part, "*", "/") # find the index of the first instance of * or /
        if part[i] == "*": # if mult
            result = part[i - 1] * part[i + 1] # calculate the product
        else: # otherwise div
            result = part[i - 1] / part[i + 1] # calculate quotient
        part.pop(i) # remove the evaluated vals
        part.pop(i) # remove the evaluated vals
        part[i - 1] = result # input the result in place
        return part # return the manipulated array
    
    def addition_or_subtraction(self, part):
        '''return the inputted array with the first addition or subtraction evaluated'''
        i = self.find(part, "+", "-")  # find the index of the first instance of + or -
        if part[i] == "+": # if addition
            result = part[i - 1] + part[i + 1] # calculate the sum
        else: # otherwise subtraction
            result = part[i - 1] - part[i + 1] # calculate the difference
        part.pop(i) # remove the evaluated vals
        part.pop(i) # remove the evaluated vals
        part[i - 1] = result # input the result in place
        return part # return the manipulated array

    def order_emdas(self, part):
        '''given an expression list without parentheses evaluate it
        exponents, then multiplication and division, then addition and subtraction'''

        # for the number of times an exponent appears:
        for i in range(self.find_num_of_occurances(part, "^")): 
            # evaluate the first instance of expoenent
            part = self.exponents(part)

        # for the number of times a mult or div appears
        for i in range(self.find_num_of_occurances(part, "*","/")):
            # evaluate the first instance of mult or div
            part = self.multiplication_or_division(part)
        
        # for the number of times a add or sub appears
        for i in range(self.find_num_of_occurances(part, "+","-")):
            # evaluate the first instance of add or sub
            part = self.addition_or_subtraction(part)

        # length of part should be 1 so we can return whats left, the evaluated statement
        return part[0]

if __name__ == '__main__':
    method = Eval("(22 + (17) + (14)) + 69 * 23 + (32 / 2 + (12 + 4))")
    print(method)
    solution = method.order_emdas(method.expression_list)
    print(solution)
    print(method.order_emdas([12, '*', 23, '/', 34, '^', 45, '-', 8]))
