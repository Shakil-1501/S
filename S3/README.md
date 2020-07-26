
  ###### Author Info :
   
- Mail : [jagatabhay@gmail.com](jagatabhay@gmail.com)


# Session3 - Numeric Types
### Objective : To pass the test cases , where to emaulate inbuilt math module with restriction of not using math module.

##### *Getting Started*

To pass the test cases 5 functions are desinged
- [encoded_from_base10](#encoded_from_base10)
- [float_equality_testing](#float_equality_testing)
- [manual_truncation_function](#manual_truncation_function)
- [manual_rounding_function](#manual_rounding_function)
- [rounding_away_from_zero](#rounding_away_from_zero)

---





### encoded_from_base10
> Parameters :  number, base, digit_map. 

> Return : String.

> This function returns a string encoding in the "base" for the the "number" using the "digit_map".


Below conditions are required or must posses:
1. 2 <= base <= 36 else raise ValueError.
1. Invalid base ValueError must have relevant information.
1. Digit_map must have sufficient length to represent the base.
1. Function must return proper encoding for all base ranges between 2 to 36 (including).
1. Function must return proper encoding for all negative "numbers" (hint: this is equal to encoding for +ve number, but with - sign added).
1. digit_map must not have any repeated character, else ValueError.
1. Repeating character ValueError message must be relevant
1. ***You cannot use any in-built functions in the MATH module***.
1. Inbuilt functions like 'bin(' , 'hex(' is strictly prohibited.





---

### float_equality_testing
> Parameters : a , b (Two fractions number)

> Return : Boolean

This function emulates the ***isclose**** method from the ***math*** module , with a restriction of not importing ***math*** module.

If so one of the test cases will fail.

***isclose*** methods returnd ***True*** if the values a and b are close ( or equality ) to each other and ***False*** otherwise.

Whether or not two values are considered close is determined according to given absolute and relative tolerances. (mentioned below).


Assumptions
1. Relative Tolerance (rel_tol) : 1e-12
1. Absolute Tolerance (abs_tol) : 1e-5



[Back To Top](#session3---numeric-types)

---

### manual_truncation_function
> Parameter : f_num (number).

> Return : formatted truncated number.

 This function emulates python's ***trunc*** method from ***math*** , with a restriction of not importing ***math*** module.
 
 If so one of the test cases will fail.
 
 ***trunc***  method performs  truncation and return the real value of number ( int )
 
 
 
 [Go To Bottom](#results)

---


### manual_rounding_function
> Parameter : f_num (number).

> Return : formatted round number.

This function emulates python's inbuild ***round*** function. You are not allowed to use ROUND function.

If so one of the test cases will fail.

This round method round a number to a given precision in decimal digits.


---

### rounding_away_from_zero
> Parameters : f_num (fraction number)

> Return : fraction numerator

This function implements rounding away from zero as covered in the class


[Back To Top](#session3---numeric-types)

---

### Files

Respective modified methods are implemented and files links are shared below.

- Code - [Method Implementation](https://github.com/jagatabhay/EPAi/blob/master/S3/session3.py)
- Test Cases - [.py File](https://github.com/jagatabhay/EPAi/blob/master/S3/test_session3.py)
- Colab -  [Test Results](https://github.com/jagatabhay/EPAi/blob/master/S3/Session_3.ipynb)


### Results
  
 
| Serial Number  | Test Cases | Outputs |
| ------------- | ------------- |-------- |
|  1 | README File Exists  | Pass    |
| 2 |  READEME contain desciption | Pass |
| 3  | README proper description  | Pass    |
| 4 | README formating count(#) > 10  | Pass |
|  5 | Indentations follow PEP8 guidelines | Pass    |
| 6 | Function name should not have caps letter | Pass |
| 7  | Invalid base ValueError   | Pass    |
| 8 | Invalid base ValueError should provide relevant message | Pass |
|  9 | Inaccurate digit map length  | Pass    |
| 10 | Emulate inbuilt hexadecimal conversion | Pass |
| 11  | Emulate inbuilt negative hexadecimal conversion | Pass    |
| 12 |  Repeating digits in digit map | Pass |
| 13 | Repeating digits valueerror should provide relevant message  | Pass    |
| 14 | Emulate inbuilt math.isclose()  | Pass |
| 15 | Restrict usage of inbuilt function  | Pass    |
| 16| Import fraction module | Pass |
| 17 | Emulate inbuilt math.trunc()  | Pass    |
| 18 | Emulate inbuilt math.round  | Pass |
| 19 | Check all emaultes for zero  | Pass    |

 
---



[Back To Top](#session3---numeric-types)
