def roots(a, b, c):
    radicando = b**2-4*a*c
    raizP = (-b+((radicando)**(1/2)))/2*a
    raizN = (-b-((radicando)**(1/2)))/2*a

    if (radicando<0):
        return "( )"
    elif (raizP == raizN):
        return f"({raizP})"
    else:
        return f"({raizP}, {raizN})"


def value_y(a, b, c, x):
    
    return (a*(x**2) + b*x + c)


def to_string(a, b, c):

    return f"f(x) = {a} * X^2 + {b} * X + {c}"


def derivation(a, b, c):

    return f"f'(x) = {2*a}X + {b}"

print(roots(1,-3,2))
print(value_y(1,-3,2,-1))
print(to_string(2,-3,1))
print(derivation(2,-3,1))
