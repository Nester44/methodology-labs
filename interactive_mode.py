from solve_equation import solve_equation

def entry (k):
    response = input(f'{k} = ')
    try:
        number = float(response)
    except:
        print(f'Error. Expected a valid real number, got {response} instead')
        return entry(k)
    return number

def main():
    a, b, c = entry('a'), entry('b'), entry('c')
    if a:
        return solve_equation(a, b, c)
    else:
        print('a cannot be 0')
        return solve_equation()