# 2+3
# Token(NUMBER, 2) Token(PLUS, "+") Token(NUMBER, 3)

# Tokens
# numbers = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# minus = -
# plus = +


from enum import Enum


ALLOWED_CHARACTERS = "0123456789+-/*x"


class InvalidTokenError(Exception):
    pass


class Tokens(Enum):
    NUMBERS = "NUMBERS"
    MINUS = "MINUS"
    PLUS = "PLUS"
    NULL = "NULL"


class Token:
    def __init__(self, tipo, value):
        self.type = tipo
        self.value = value
    
    def __str__(self):
        return f"Token({self.type.value}, {self.value})"


class Lexer:
    def reset(self, string):
        self.string = string
        self.current_char_position = 0

    def get_next_token(self):
        while self.current_char_position < len(self.string):
            if self.string[self.current_char_position].isdigit():
                token = Token(Tokens.NUMBERS, int(self.string[self.current_char_position]))
                self.current_char_position += 1
                return token
            if self.string[self.current_char_position] == "+":
                token = Token(Tokens.PLUS, "+")
                self.current_char_position += 1
                return token
            if self.string[self.current_char_position] == "-":
                token = Token(Tokens.MINUS, "-")
                self.current_char_position += 1
                return token

        return Token(Tokens.NULL, None)


class Interpreter:
    def __init__(self):
        self.lexer = Lexer()
        self.current_token = None
    
    def eat(self, _type):
        if _type == self.current_token.type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise InvalidTokenError("Invalid token type")
    
    def factor(self):
        number = self.current_token
        self.eat(Tokens.NUMBERS)
        return number.value
    
    # 3 + 3 -> Factor + Factor| 4 - 6 -> Factor - Factor 
    def term(self):
        left = self.factor()

        op = self.current_token
        if op.type == Tokens.PLUS:
            self.eat(Tokens.PLUS)
        if op.type == Tokens.MINUS:
            self.eat(Tokens.MINUS)
        
        right = self.factor()

        if op.type == Tokens.PLUS:
            result = left + right
        if op.type == Tokens.MINUS:
            result = left - right

        return result

    # for division and multiplication with arbitrary operands and operators: 2*2/4*2/3
    def term_2():
        # Tomar un factor y guardarlo en un acomulado
        while # you have to check the the next token is one operator and if not you quit the loop:
            # tomar operador
            # tomar factor
            # hacer el calculo
            pass

    # 3 + 2

    def eval(self, string):
        self.lexer.reset(string)
        self.current_token = self.lexer.get_next_token()

        factor = self.term_2()
        return factor


def main():
    string = ""

    calculator = Interpreter()
    while string.lower() != "x":
        try:
            string = input("calculate>>> ")

            condition = [char in ALLOWED_CHARACTERS for char in string]
            if not all(condition):
                print("You are using not allowed characters")
                continue
            
            result = calculator.eval(string)
            print(result)

        except InvalidTokenError as e:
            print(f"Syntax error: {string}")
        except KeyboardInterrupt as e:
            break

    print("\nBye, thanks for using our calculator")


if __name__ == "__main__":
    main()
