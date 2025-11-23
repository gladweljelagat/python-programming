# Assignment Two

Requirements:

 Allowed editors: vi , vim , emacs

 All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3

 All your files should end with a new line

 The first line of all your files should be exactly #!/usr/bin/python3

 A README.md file, at the root of the folder of the project, is mandatory

 Your code should use the pycodestyle (version 2.8.* )

 All your files must be executable

 The length of your files will be tested using wc


## Task 0

Safe list printing

 0-safe_print_list.py: Python function that prints x elements of a list on the same line,followed by a new line.

 The parameter x represents the number of elements to print - can be bigger than the length of my_list.

 Returns the real number of elements printed.

 Without importing modules or using len()



## Task 1

Safe printing of an integers list

 1-safe_print_integer.py: Python function that prints an integer
in &quot;{:d}&quot;.format() format.

 The parameter value can be any type.

 Returns True if value was printed correctly (ie. was an integer), False otherwise.

 Without importing modules or using type().


## Task 2

Print and count integers

 2-safe_print_list_integers.py: Python function that prints the first x elements of a list that are integers on the same line, followed by a new line.

 The parameter my_list can contain any type.

 The parameter x represents the number of elements to print - can be bigger than the length of my_list.

 Reutnrs the real number of integers printed.

 Without importing modules or using len()


## Task 3

Integers division with debug

 3-safe_print_division.py: Python function that divides two integers and prints the result

using finally:.

 The function assumes that the arguments are integers.

 Upon success, returns the value of the division; otherwise - returns None.

 Without importing modules.


## Task 4

Divide a list

 4-list_division.py: Python function that divides two lists element by element.

 Returns a new list of length list_length with all divisions.

 The lists my_list_1 and my_list_2 can contain any type.

 The parameter list_length can be larger than the lengths of either list.

 If an element is not an integer or float, the function prints wrong type.

 If the division cannot be done, the result of the division is 0 and the function

prints: division by 0.

 If either of my_list_1 or my_list_2 are too short, the function prints: out of range.

 Without importing modules.


## Task 5

Raise exception

 5-raise_exception.py: Python function that raises a type exception.

 Without importing modules.


## Task 6

Raise a message

 6-raise_exception_msg.py: Python function that raises a name exception with a
message.

 Without importing modules.


## Task 7

Safe integer print with error message

 100-safe_print_integer_err.py: Python function that prints an integer with type-checking in &quot;{:d}&quot;.format()) format.

 The paramter value can be any type.

 Returns True if value was printed correctly (ie. was an integer).

 Otherwise, prints an exception error to stderr and returns False.

 Without importing modules.


## Task 8

 Safe function

o 101-safe_function.py: Python function that executes a function safely.

o The function assumes that the paramter fct is always a pointer to a function.

o Upon success, returns the result of the function.

o Otherwise, prints an exception error to stderr and returns None.
