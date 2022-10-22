from nodes import Nodes as nodes

DIGITS = '0123456789'

K_PLUS = '+'

class Calculation:
    def __init__(self, chars):
        self.chars = chars

    def get_token(self, chars):
        tokens = []
        index = 0
        for char in chars:
            if char in DIGITS:
                currect_token = str(char)
                if index - 1 > -1 or index - 1 == 0:
                    last_index = index - 1
                    if str(tokens[last_index]).isdigit():
                        last_digit = tokens[last_index]
                        tokens.pop(last_index)
                        tokens.append(str(last_digit ) + str(currect_token))
                        continue

                tokens.append(currect_token)
                
            elif char == K_PLUS:
                currect_token = str(K_PLUS)
                tokens.append(currect_token)

            index += 1

        return tokens

    def get_number_tokens(self, tokens):
        number_tokens = []
        for char in tokens:
            if char.isdigit():
                if type(char) == str:
                    number_tokens.append(int(char))
            else:
                continue
        
        return number_tokens

    def check_token(self, tokens):
        number_token = self.get_number_tokens(tokens)
        #always plus
        index = 0
        for elem in number_token:
            if index == 1:
                base = number_token[0]
                diff = number_token[1]
                if base == 9 or base == 10:
                    if diff == 9 or diff == 10:
                        print(21)
                    else:
                        print(nodes.add(base, diff))
                else:
                    print(nodes.add(base, diff))

            index += 1

            




