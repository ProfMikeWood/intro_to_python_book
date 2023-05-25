# Control Flow

## Check your understanding

1. Which of the following can you use to end a control flow statement?  
	a. Reduce the indentation level   
	b. Closed curley brace `}`  
	c. Closed parentheses `)`  
	d. The `end` keyword  

2. Which of the following can be used as an iterator in a for loop?  
	a. lists  
	b. a range of integers  
	c. string  
	d. all of the above  

3. Define `x = [5, 6, 7, 8, 9]`. Which of the following prints the numbers 5, 6, 7, 8, 9, each on a separate line?  
	a.
	```
	for n in range(len(x)):
            print n
	```  
	b.
	```
	for j in x:
            print x
	```
	c.
	```
	for k in range(5,9):
            print k
	```  
	d.
	```
	for k in range(5,10):
            print k
	```  

4. The \_\_\_\_\_\_\_\_\_\_ statement will terminate a loop when it is reached while the \_\_\_\_\_\_\_\_\_\_ statement will terminate a particular iteration of the loop.  
	a. break, break  
	b. break, continue  
	c. continue, break  
	d. continue, continue  

5. Define `list1 = ['Hello','World']` and `list2 = [j[0] for j in list1]`. Which of the following yields an equivalent list2?  
	a. `list2 = list1[0][0] + list1[1][0]`  
	b. `list2 = ['h','w']`  
	c. 
	```
	list2 = []
	for j in list1:
	    list2.append(j[0])
	```
	d. `list2 = list1[:][:1]`

6. What character do you use to split long strings across lines?  
	a. `:`  
	b. `\n`  
	c. `/`  
	d. `/`

7. What boolean comparison can you use to check two conditions?  
	a. `logical_and`  
	b. `&&`  
	c. `and`  
	d. `||`
