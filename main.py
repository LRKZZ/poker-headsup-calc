import holdem_calc
import os
from dotenv import load_dotenv
import ast

load_dotenv()

list_string = os.getenv('LIST')
list_array = ast.literal_eval(list_string)

board_string = os.getenv('BOARD')
board = ast.literal_eval(board_string)



odds = holdem_calc.calculate(board, False, 10, None, list_array, True)
print(odds)
