# Functions

## Check your understanding

1. What is the best way to provide a human-readable synopsis of a function?  
	a. provide comments with # symbols throughout your code  
	b. provide a docustring comment on the first line of the function  
	c. name the function a descriptive name  
	d. write a separate documentation file to provide a summary of the function  

2. What is the main way you can pass arguments to a function?  
	a. pass arguments in the orfer they are defined  
	b. pass arguments by giving the name of the variable  
	c. pass argumnts as a list or a dictionary  
	d. all of the above  

3. What is the difference between a function `func` defined with `func(*args)` vs `func(**args)`?  
	a. the latter option is the same as the first but the valueds are squared  
	b. the latter option can be a list of variable size while the former is a list of fixed size  
	b. the latter option puts arguments into a dict while the former puts them into a list  
	d. the latter option puts arguments into a list while the former puts them into a dict  

4. Which of the following would modify the object or variable stored in `x`?  
	a.   
	```
	x = {1: "one", 2: "two"}
	def add_three(x):
		x[3] = "three"
	```
	b.   
	```
	x = 1
	def add_three(x):
		x += 3
	```
	c.   
	```
	x = "one"
	def add_three(x):
		x = x + " three"
	```
	d.   
	```
	x = (1, 2)
	def add_three(x):
		x[0] += 3
		x[1] += 3
	```

5. Consider the following code:
```
a = 2
def add_number(integer):
	a = a + integer
print(a)
```
	a. Traceback (error) because `a` is not defined inside `add_number`.  
	b. The function will run but `a` will not change since the operation is local.  
	c. The function will look into the global scope, find `a` and add an integer.  
	d. The function will raise a warning because `a` is not defined in the function, but there will not be a traceback error.  

6. What is a `lambda` function?  
	a. an abstract function  
	b. a function with only one output  
	c. a function with only one input argument  
	d. an inline function  

7. What keyword indicates that a function is a generator?  
	a. yield  
	b. return  
	c. generate  
	d. while 
