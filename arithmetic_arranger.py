import re

def arithmetic_arranger(problems, solve=False):
    """ Arranges a list of arithmetic problems vertically """

    split_problems = [split_problem(p) for p in problems]
    error = check_problem_set_for_errors(split_problems)

    if error:
        return error

    if solve:
        split_problems = [add_solution(p) for p in split_problems]

    vertical_problems = [arrange_vertically(p) for p in split_problems]
    arranged_problems = arrange_problems(vertical_problems)

    return arranged_problems


def split_problem(problem): 
    """ Split a problem into a tuple of its parts, such as ('32', '+', '47') """
    return tuple(problem.split())


def check_problem_set_for_errors(problems):
    """ 
    Checks a problem set for errors and returns either None 
    or a string desribing the first error found. 
    """

    if len(problems) > 5:
        return "Error: Too many problems."
    
    for problem in problems:
        error = check_for_error(problem)
        if error:
            return error

    return None


def check_for_error(problem):
    """ 
    Checks a problem for errors and returns either None 
    or a string desribing the first error found. 
    """

    (x, op, y) = problem

    if not is_operator_valid(op):
        return "Error: Operator must be '+' or '-'."
    if not is_digits_only(x) or not is_digits_only(y):
        return "Error: Numbers must only contain digits."
    if not is_length_ok(x) or not is_length_ok(y):
        return "Error: Numbers cannot be more than four digits."

    return None


def add_solution(problem):
    """ 
    Solves the problem and returns a 4-item tuple including the solution
    Example:  
    >>> add_solution(('32','+','43')) 
    ('32','+','43','75)
    """
    (x, op, y) = problem

    if op == "+":
        solution = str(int(x) + int(y))
    else:
        solution = str(int(x) - int(y))

    return (x, op, y, solution)


def arrange_vertically(problem):
    """ Returns a tuple of problem part strings with the padding needed to align the problem vertically """

    (x, op, y, *z) = problem
    max_length = max(len(x), len(y))

    top = x.rjust(max_length + 2, ' ')
    middle = op + ' ' + y.rjust(max_length, ' ')
    separator = '-' * (max_length + 2)

    if len(z) == 0:
        return (top, middle, separator)
    else:
        bottom = z[0].rjust(max_length + 2, ' ')
        return (top, middle, separator, bottom)


def arrange_problems(padded_problems):
    """ Returns a multi-line string of the padded problems arranged side-by-side"""

    arranged = "    ".join([x[0] for x in padded_problems]) + "\n"
    arranged += "    ".join([x[1] for x in padded_problems]) + "\n"
    arranged += "    ".join([x[2] for x in padded_problems])

	# include solution line if populated
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
