class Eval():
    def __init__(self, expression_string):
        '''break up this expression into a list'''
        self.expression_string = expression_string
        self.expression_list = self.expression_string_to_list(expression_string)

    def __repr__(self):
        return self.expression_string

    def expression_string_to_list(self, expression_string):
        symbols = set([*"^*/+-"])
        expression_list = []
        for char in expression_string:
            if char in symbols:
                expression_list.append(char)
            elif char.isdigit():
                if len(expression_list) > 0 and type(expression_list[-1]) == int:
                    expression_list[-1] = int(str(expression_list[-1]) + char)
                else:
                    expression_list.append(int(char))
        return expression_list

    def order_emdas(self, part):
        '''given an expression list without parentheses evaluate it'''
        exponents = []
        mult_or_divs = []
        add_or_sub = []
        for i, char in enumerate(part):
            if char == '^':
                exponents.append(i)
            elif char == '*' or char == '/':
                mult_or_divs.append(i)
            elif char == '+' or char == '-':
                add_or_sub.append(i)

        while len(exponents) != 0:
            i = exponents[0]
            # i is the index of each exponenet
            result = part[i - 1] ** part[i + 1]
            part.pop(i)
            part.pop(i)
            part[i -1] = result

            placeholder = []
            for num in exponents:
                if num > i:
                    placeholder.append(num - 2)
            exponents = placeholder
            
            placeholder = []
            for num in mult_or_divs:
                if num < i:
                    placeholder.append(num)
                if num > i:
                    placeholder.append(num - 2)
            mult_or_divs = placeholder

            placeholder = []
            for num in add_or_sub:
                if num < i:
                    placeholder.append(num)
                if num > i:
                    placeholder.append(num - 2)
            add_or_sub = placeholder

        while len(mult_or_divs) != 0:
            i = mult_or_divs[0]
            # i is the index of each exponenet
            if part[i] == '*':
                result = part[i - 1] * part[i + 1]
            else:
                result = part[i - 1] / part[i + 1]
            
            part.pop(i)
            part.pop(i)
            part[i -1] = result

            placeholder = []
            for num in mult_or_divs:
                if num > i:
                    placeholder.append(num - 2)
            mult_or_divs = placeholder

            placeholder = []
            for num in add_or_sub:
                if num < i:
                    placeholder.append(num)
                if num > i:
                    placeholder.append(num - 2)
            add_or_sub = placeholder

        while len(add_or_sub) != 0:
            i = add_or_sub[0]
            # i is the index of each exponenet
            if part[i] == '+':
                result = part[i - 1] + part[i + 1]
            else:
                result = part[i - 1] - part[i + 1]
            part.pop(i)
            part.pop(i)
            part[i -1] = result

            placeholder = []
            for num in add_or_sub:
                if num > i:
                    placeholder.append(num - 2)
            add_or_sub = placeholder
        return part[0]

    def for_the_win(self):
        no_parentheses = self.p_of_pemdas(self.expression_list)
        return self.order_emdas(no_parentheses)

if __name__ == '__main__':
    method = Eval("(22 + (17) + (14)) + 69 * 23 + (32 / 2 + (12 + 4))")
    print(method)
    solution = method.order_emdas(method.expression_list)
    print(solution)

