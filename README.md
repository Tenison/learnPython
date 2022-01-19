# learnPython

### Topics Covered so far:

<ol>
	<li><b>Variables and Print</b></li>
	<li><b>Functions</b></li>
	<li><b>Input from User</b></li>
	<li><b>Conditional Statments</b></li>
	<li><b>Loops</b></li>
	<li><b>Study Project - numberClassification</b></li>
	<li><b>Data Structures</b></li>
</ol>

##

## Variables and Print

<ul>
	<li>Integer [98]</li>
	<li>Float [9.99]</li>
	<li>String ['Hello world']</li>
	<li>Boolean [True/False]</li>
</ul>

* ___Example :___
__Strings__

```python

	'These allow "double quoting" without "escape" characters.'

	"These allow embedded 'single quoting', so you don't have to use an 'escape' character".

	'If needed, a \'slash\' can be used as an escape character within a string when switching quote styles won\'t work.'
```

__Multi-line strings are declared with `'''` or `"""`.__


```python
	'''Three single quotes or "double quotes" in a row allow for multi-line string literals.
  	Line break characters, tabs and other whitespace are fully supported.

  	You\'ll most often encounter these as "doc strings" or "doc tests" written just below the first line of a function or class definition.
    	They\'re often used with auto documentation ✍ tools.
    	'''
```

## Functions

* Use __def__ to declare a function

```python
	def example_function (Parameters):
		##Perform action
		print(f"We can print {Parameters} here!!!");
```

* Function can __return values__ or have __side effect__

__Side Effect__

```python
	def example_function (Parameters):
		##Side effect below
		print(f"We can print {Parameters} here!!!");
```

__Return Value__

```python
	def example_function (Parameters):
		return Parameter
	
	## return value from the function is stored in a variable
	hold_results = example_function(3)
```

##### Scoping (local and global)
### Input from User 
##### type casting [int(),float(),str()]
### Conditional Statments (if, switch, and try)
##### input validation
##### try::except::else::finally
##### python condition functions (isdigit() , typr()) :->
###### isdigit() only accepts positive integers
###### type() check the type of variable stored (int, float, string)
## Loops

__While loops__

* Perform the loop till __user_name__ is equal to __exit__

```python
	while user_name != "exit":
```

* Perform the loop till __number__ is equal to __5__

```python 
	while number != 5:
```

__For loops__

* range function provides a counter or list of numbers ( From __0__ to __n-1__ )

```python
	for count in range(5) :
		print(count)
```
* range function can also have multiple inputs (__start_number__, __end_number__, __interval__)

```python
	for count in range(10,20,2) :
		print(count)
```

* looping through a list 

```python
	item_list = [2,3,55,5,44,2343,54,576]

	for value in item_list :
		print(value);
```

* Printing the index of each member in the list, using __len__ and __range__ which starts from zero(0) 
\'
```python
	item_list = [2,3,55,5,44,2343,54,576]

	for value in range(len(item_list)) :
		print(value);
```

## Data Structures

__Lists__

```python
	item_list = [2,3,55,5,44,2343,54,576]
	
	## below provides the lenght of the list. Example :- output : n-1
	print(len(item_list))
```

