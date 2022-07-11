# This entrypoint file to be used in development. Start by reading README.md
from pytest import main

# from arithmetic_arranger import arithmetic_arranger
# from arithmetic_arranger import solve
import arithmetic_arranger


print(arithmetic_arranger.arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]), True)
# print(arithmetic_arranger.parse('32 + 698'))
# print(arithmetic_arranger.pad_problem(('32', '+', '698', '1024'), True))


# Run unit tests automatically
# main(['-vv'])
