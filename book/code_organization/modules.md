# Modules

## Check your understanding

1. What is a module?  
	a. a set of files that comprise a series of similar functions  
	b. a single script that has related objects  
	c. a single script that excusively relies on lower level C or C++ code  
	d. another name for a package  

2. Say you have a module called `earth.py` with a method `getPopulation`. How can you import this module and call the method?  
	a.  
	```
	import earth.py
	x = getPopulation()
	```  
	b.  
	```
	x = earth.getPopulation()
	```  
	c.  
	```
	from earth import getPopulation
	x = getPopulation()
	```  
	d.  
	```
	import earth
	x = getPopulation()
	```   

3. What is the difference between the statements `import module` and `from module import *`?  
	a. some public methods aren't available with `from module import *`  
	b. functions from `import module` will need the module name prepended when they are called  
	c. functions from `from module import *` will need the module name prepended when they are called  
	d. they are exactly the same  

4. Where does Python look for moduules?  
	a. a lit of dictionaries stores in sys.path  
	b. the local directory  
	c. a list of directories stores in your operating system's variable `PYTHONPATH`  
	d. all of the above  

5. What can you do to write "private" methods in a module -- methods that can't be accessed outside of the module?  
	a. use the `private` keyword  
	b. start the function with an underscore (`\_`)  
	c. use the @private annotation   
	d. you can't have private functions in a module  

6. When the value of a variable `x` is referencd (e.g. `print(x)`), where does Python look for the reference to the variable `x`?  
	a. first the local namespace, then the global namespace, then the built-in namespace  
	b. first the built-in namespace, then the local namespace, then the global namespace  
	c. first the global namespace, then the local namespace, then the built-in namespace  
	d. first the global namespace, then the build-in namespace, then the local namespace  

7. What happens if you define a function or a variable name that is built into Python (e.g. a variable or function named `print`)?  
	a. NameError  
	b. TypeError  
	c. ValueError  
	d. The new function or variable overrides the bult-in function or variable