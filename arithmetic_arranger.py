import re


def arithmetic_arranger(problems, solve=False):
    """ Arranges a list of arithmetic problems vertically """

    problem_parts = [convert_to_parts(p) for p in problems]

    error = check_problem_set_for_errors(problem_parts)

    if error:
        return error

    if solve:
        problem_parts = [solve_problem(p) for p in problem_parts]

    # pad each problem to the correct string length
    padded = [pad_problem(p) for p in problem_parts]

    return arrange_problems(padded)

def convert_to_parts(problem): 
    return tuple(problem.split())

def check_problem_set_for_errors(problems):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    for problem in problems:
        error = check_for_error(problem)
        if error:
            return error

def check_for_error(problem):
    (x, op, y) = problem

    if not is_operator_valid(op):
        return "Error: Operator must be '+' or '-'."
    if not is_digits_only(x) or not is_digits_only(y):
        return "Error: Numbers must only contain digits."
    if not is_length_ok(x) or not is_length_ok(y):
        return "Error: Numbers cannot be more than four digits."

    return None


def solve_problem(problem):
    (x, op, y) = problem

    if op == "+":
        solution = str(int(x) + int(y))
    else:
        solution = str(int(x) - int(y))

    return (x, op, y, solution)

def pad_problem(problem):
    x = problem[0]
    op = problem[1]
    y = problem[2]
    max_length = max(len(x), len(y))

    top = x.rjust(max_length + 2, ' ')
    middle = op + ' ' + y.rjust(max_length, ' ')
    line = '-' * (max_length + 2)

    if len(problem) == 4:
        bottom = problem[3].rjust(max_length + 2, ' ')
        return (top, middle, line, bottom)
    else:
        return (top, middle, line)

def arrange_problems(padded_problems):
    arranged = "    ".join(map(lambda x: x[0], padded_problems)) + "\n"
    arranged += "    ".join(map(lambda x: x[1], padded_problems)) + "\n"
    arranged += "    ".join(map(lambda x: x[2], padded_problems)) 

    if len(padded_problems[0]) == 4:
        arranged += "\n" + "    ".join(map(lambda x: x[3], padded_problems))

    return arranged 


def is_operator_valid(op):
    return op in ['-', '+']


def is_digits_only(number):
    if re.search("^\d*$", number):
        return True
    else:
        return False


def is_length_ok(number):
    return len(number) <= 4
