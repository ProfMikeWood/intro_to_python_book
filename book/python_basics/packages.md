# Packages


## Check your understanding

1. What is a package?  
	a. a single file with related functions  
	b. a pre-compiled set of code  
	c. a directory containing related modules  
	d. a 

2. Packages can organize files into a directory structure with several subdirectories. When importing a module from a package subdirectory, what delimiter is used for the relative path components?  
	a. `/`  
	b. `\`  
	c. `,`  
	d. `.`  

3. When files are placed in a directory to form a package, what must be done to ensure the files form a package?  
	a. the package name must be placed in the header of each file  
	b. the files must be zipped into a `.pkg` file  
	c. each directory in the package must contain an `__init__.py` file  
	d. each file must be explicitly added to the `PYTHONPATH`  

4. Suppose you have a package module that needs to import a module 2 levels up its directory tree. Which of the following statements can be used to define a relative path 2 levels up?  
	a. `..`  
	b. `....`  
	c. `../../`  
	d. `^^`

5. When calling `from mymodule import *`, which of the following is true?  
	a. the statement will import all files in the current directory  
	b. the statement will import all files in the current directory except those starting with an underscore  
	c. the statement will import all files listed in the ``__all__`` list of the ``__init__.py`` script  
	d. the statement will import files in the current directory and all subdirectories

