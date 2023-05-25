---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Object Types

## Check your understanding

1. How can you check the type of an object `x`?  
	a. `type(x)`  
	b. `x.type()`  
	c. `sys.type(x)`  
	d. `os.type(x)`  

2. How can you retrieve the name of the class that generates an object `x`?  
	a. `x.__classname__`  
	b. `x.__class__.__name__`  
	c. `x.__getname__`  
	d. `x.__getclass__`


3. What is the difference between `isinstance` and `type`?  
	a. `isinstance` returns the class name while `type` returns an object  
	b. `isinstance` returns an object while `type` returns the class name
	b. `isinstance` returns a Boolean while `type` returns an object  
	c. `isinstance` returns an object while `type` returns a Boolean value

4. When defining a class, what method can be used to define a human-readable string output when print objects?  	
	a. use the `@Override` annotation  
	b. use the `@Property` annotation  
	c. write a method called `_to_str`  
	d. write a method called `__str__`  

5. When the `list` class retrieves an object from a list using an index in backets (e.g. `my_list[2]`), what underying *special method attribute* is called?  
	a. `__get__`  
	b. `__getitem__`  
	c. `__retrieve__`  
	d. `__retrieveitem__`  

6. Suppose you wanted to create a dictionary class where all keys were required to be the same type. What options are available in Python to create this class?    
	a. Write a new class with all of the same methods as the dict class  
	b. Write a subclass of the `dict` class with new methods for `__getitem__` and `__setitem__`  
	c. Write a subclass of the `UserDict` class with new methods for `__getitem__` and `__setitem__`  
	d. All of the above  



