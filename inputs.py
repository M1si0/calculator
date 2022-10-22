from calculator import Calculation

while True:
    text = input("calc >> ")
    calculation = Calculation(text)
    tokens = calculation.get_token(text)
    num_toks = calculation.check_token(tokens)