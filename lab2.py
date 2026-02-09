#assigning integer literls to variables
integer1 = 10
integer2 = -5
integer3 = 0

print("integer values:")
print("integer1 =", integer1)
print("integer2 =", integer2)
print("integer3 =", integer3)

#performing operations on integer literals
print("sum of integer1 and integer2:", integer1 + integer2)
print("product of integer1 and 3:", integer1 * 3)
print("difference between integer1 and integer2:", integer1 - integer2)

#assigning floating-point literals to variables
float1 = 3.14
float2 = -2.718
float3 = 0.0

#performing operations with floating-point numbers
sum_floats = float1 + float2
product_floats = float1 * 2
difference_floats = float1 - float2

#printing floating-point values and results of operations
print("\nfloating-point values:")
print("float1 =", float1)
print("float2 =", float2)
print("float3 =", float3)
print("sum of float1 and float2:", sum_floats)
print("product of float1 and 2:", product_floats)
print("difference between float1 and float2:", difference_floats)

#assigning complex literals to variables
complex1 = 2 + 3j
complex2 = -1 - 4j
complex3 = 0 + 0j

#performing operations with complex numbers
sum_complex = complex1 + complex2
product_complex = complex1 * (1 + 1j)
difference_complex = complex1 - complex2

#printing complex values and results of operations
print("\ncomplex values:")
print("complex1 =", complex1)
print("complex2 =", complex2)
print("complex3 =", complex3)
print("sum of complex1 and complex2:", sum_complex)
print("product of complex1 and (1 + 1j):", product_complex)
print("difference between complex1 and complex2:", difference_complex)

#single-quoted strings
single_quoted = 'hello, world!'

#string operations with single-quoted strings
length = len(single_quoted)  #length of the string
upper_case = single_quoted.upper() #convert to upercase
lower_case = single_quoted.lower() #convert to lowercase
contains_substring = 'world' in single_quoted  #check if substring is present

#printing results
print("single-quoted string:", single_quoted)
print("length of the string:", length)
print("uppercase version:", upper_case)
print("lowercase version:", lower_case)
print("contains 'world':", contains_substring)

#double quoted string
double_quoted = "edunet is awesome!"

#string operations
length = len(double_quoted)  #length of the string
replaced_string = double_quoted.replace("awesome", "great")  #replace word
word = double_quoted.split()  #split into words

#printing results
print("double-quoted string:", double_quoted)
print("length of the string", length)
print("string after replacement:", replaced_string)
print("words in the string:", word)

#define a string and an integer
string_value = "the number is"
integer_value = 42

#convert the integer to a string using explicit conversion
integer_as_string = str(integer_value)

#concatenate the string and the converted integeresult
result = string_value + integer_as_string

#print the result
print(result)

#define two numbers
a = 15
b = 4

#addition
addition_result = a + b
print("addition:{} + {} = {}".format(a, b, addition_result))

#subtraction
subtraction_result = a - b
print("subtraction: {} - {} = {}".format(a, b, subtraction_result))

#multipication
multiplication_result = a * b
print("multiplication: {} * {} = {}".format(a, b, multiplication_result))

#division
division_result =a / b
print("division: {} // {} = {:.2f}".format(a, b, division_result))

#floor division
floor_division_result = a // b
print("floor division: {} // {} = {}".format(a, b, floor_division_result))

#modulus
modulus_result = a % b
print("modulus: {} % {} = {}".format(a, b, modulus_result))

#exponentiation
exponentiation_result = a ** b
print("exponentiation: {} ** {} = {}".format(a, b, exponentiation_result))
