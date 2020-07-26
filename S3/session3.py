from fractions import Fraction
def encoded_from_base10(number, base, digit_map):
    '''
    This function returns a string encoding in the "base" for the the "number" using the "digit_map"
    Conditions that this function must satisfy:
    - 2 <= base <= 36 else raise ValueError
    - invalid base ValueError must have relevant information
    - digit_map must have sufficient length to represent the base
    - must return proper encoding for all base ranges between 2 to 36 (including)
    - must return proper encoding for all negative "numbers" (hint: this is equal to encoding for +ve number, but with - sign added)
    - the digit_map must not have any repeated character, else ValueError
    - the repeating character ValueError message must be relevant
    - you cannot use any in-built functions in the MATH module

    '''

    if base<2 or base>36:
        raise ValueError("The base is not correct")

    if len(digit_map)<base:
        raise ValueError

    for i in digit_map:
        if digit_map.count(i)>1:
            raise ValueError("There is repeating character in digit_map")


    digits=[]
    while number>0:
        m=number % base
        number=number // base
        digits.insert(0,m)
    resultant=''
    for d in digits:
        resultant += digit_map[d]
    '''
    while number<0:
        m=number % base
        number=number // base
        digits.insert(0,m)
        resultant=''
    for d in digits:
        resultant += digit_map[d]

    '''
    if number<0 :
        number=-number
        while number>0:
            m=number % base
            number=number // base
            digits.insert(0,m)
        resultant=''
        for d in digits:
            resultant += digit_map[d]
        resultant='-'+resultant
    return resultant


def float_equality_testing(a, b):
    '''
        This function emulates the ISCLOSE method from the MATH module, but you can't use this function
        We are going to assume:
        - rel_tol = 1e-12
        - abs_tol = 1e-05
    '''
    rel_tol=1e-12
    abs_tol=1e-05
    tol=max(rel_tol*(max(abs(a),abs(b))),abs_tol)
    if abs(a-b) < tol:
        d=True
    else:
        d=False
    return d


def manual_truncation_function(f_num):
    '''
    This function emulates python's MATH.TRUNC method. It ignores everything after the decimal point. 
    It must check whether f_num is of correct type before proceed. You can use inbuilt constructors like int, float, etc
    '''
    f_num = f_num.__trunc__()

    return f_num

def manual_rounding_function(f_num):
    '''
    This function emulates python's inbuild ROUND function. You are not allowed to use ROUND function, but
    expected to write your one manually.
    '''
    f_num = f_num.__round__()

    return f_num

def rounding_away_from_zero(f_num):
    '''
    This function implements rounding away from zero as covered in the class
    Desperately need to use INT constructor? Well you can't. 
    Hint: use FRACTIONS and extract numerator. 
    '''
    return 3.0