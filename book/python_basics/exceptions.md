# Exceptions

## Check your understanding

1. What are "exceptions" in Python?  
	a. its a warning in code that automatically triggers a fail-safe alternative code  
	b. its an error generated anywhere in the code  
	c. its an error in a code that "traces back" to the location where it originated  
	d. an object generated using an except statement  


2. Why are there different types of exceptions?  
	a. so exception handlers can respond appropriately to different types of errors  
	b. so exceptions handlers can work with different primitive types  
	c. so exception handlers can be adapted to new versions of Python  
	d. all of the above  


3. Which of the following does NOT describe Python's approach to errors?  
	a. errors are written in the easiest way possible  
	b. errors are dealt with only as they occur  
	c. errors follow the "easier to ask for forgiveness than permission" paradigm  
	d. errors are checked as often as possible before they occur  


4. What happens when an exception is raised?  
	a. the program terminates immediately  
	b. the program will not compile  
	c. the program prints a message and terminates  
	d. the program sends an exception to higher functions to see if there is an exception handler  


5. A try statement will check to see if some codes runs. If an exception is raised, what statement would run no what the exception type?  
	a. `except`  
	b. `except exception*`  
	c. `else`  
	d. `finally`  


6. What is the best way to define your own exception?  
	a. `raise MyException`  
	b. `class MyException(BaseException)`  
	c. `class MyException(Exception)`  
	d. `raise MyException(Exception)`  


7. How can you run code with assert statements?  
	a. running code with the `-O` or `-OO` options  
	b. running code with `__debug__ = true`  
	c. setting `PYTHONOPTIMIZE = True`  
	d. all of the above  


8. What is a context manager?  
	a. a way to safely open files  
	b. a concise `try`-`except` statement induced with the with keyword  
	c. a method to interpret code depending on the operating system in which its run  
	d. a method to interpret code depending on where the the code is called from on the operating system  
