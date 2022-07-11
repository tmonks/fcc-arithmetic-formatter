import re


def arithmetic_arranger(problems, solve=False):
    """ Arranges a list of arithmetic problems vertically """

    if len(problems) > 4:
        return "Error: Too many problems."

	# split and solve problems
    try:
        problem_tuples = split_and_solve(problems)
    except Exception as e:
        return str(e)

    # pad each problem to the correct string length
    padded = list(map(lambda p: pad_problem(p, solve), problem_tuples))

    return arrange_problems(padded, solve)


def split_and_solve(problems):
    return list(map(parse, problems))

def parse(problem):
    [x, op, y] = problem.split()

    if not is_operator_valid(op):
        raise Exception("Error: Operator must be '+' or '-'.")
    if not is_digits_only(x) or not is_digits_only(y):
        raise Exception("Error: Numbers must only contain digits.")
    if not is_length_ok(x) or not is_length_ok(y):
        raise Exception("Error: Numbers cannot be more than four digits.")

    return (x, op, y, solve_problem(x,op,y))


def solve_problem(x, op, y):
    if op == "+":
        return str(int(x) + int(y))
    else:
        return str(int(x) - int(y))

def pad_problem(problem, solve=False):
    (x, op, y, z) = problem
    if solve:
        max_length = max(len(x), len(y), len(z))
    else:
        max_length = max(len(x), len(y))

    top = x.rjust(max_length + 2, ' ')
    middle = op + ' ' + y.rjust(max_length, ' ')
    line = '-' * (max_length + 2)
    bottom = z.rjust(max_length + 2, ' ')

    if solve:
        return (top, middle, line, bottom)
    else:
        return (top, middle, line)

def arrange_problems(padded_problems, solve=False):
    arranged = "    ".join(map(lambda x: x[0], padded_problems)) + "\n"
    arranged += "    ".join(map(lambda x: x[1], padded_problems)) + "\n"
    arranged += "    ".join(map(lambda x: x[2], padded_problems)) + "\n"

    if solve:
        arranged += "    ".join(map(lambda x: x[3], padded_problems)) + "\n"

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


def format_problem(problem):
    max_length = get_max_length(problem)
    

def get_max_length(problem_tuple):
    return max(map(len, problem_tuple))