def calculate(expression):

    try:
        answer = eval(expression)
        return answer

    except Exception:
        return "Invalid Expression"