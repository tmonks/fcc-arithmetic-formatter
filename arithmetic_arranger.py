import re


def arithmetic_arranger(problems):
    arranged_problems = []
    if len(problems) > 4:
        return "Error: Too many problems."

    try:
        parsed = parse_problems(problems)
    except Exception as e:
        return str(e)

    return arranged_problems


def parse_problems(problems):
    parsed = []

    for problem in problems:
        [x, op, y] = problem.split()
        if not is_operator_valid(op):
            raise Exception("Error: Operator must be '+' or '-'.")
        if not is_digits_only(x) or not is_digits_only(y):
            raise Exception("Error: Numbers must only contain digits.")
        if not is_length_ok(x) or not is_length_ok(y):
            raise Exception("Error: Numbers cannot be more than four digits.")

    return parsed


def is_operator_valid(op):
    return op in ['-', '+']


def is_digits_only(number):
    if re.search("^\d*$", number):
        return True
    else:
        return False


def is_length_ok(number):
    return len(number) <= 4
