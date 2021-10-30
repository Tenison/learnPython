# learnPython

## Topics Covered so far:
## Variables and Print

<ul>
	<li>Integer (98)</li>
	<li>Float (9.99)</li>
	<li>String ("Hello world")</li>
	<li>Boolean (True/False)</li>
	<li>list</li>
</ul>

### functions
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
<ul>
	<li><b>While loops</b></li>
</ul>

__Examples__

```python
	while user_name != "exit":
```

```python 
	while number != 5:
```
<ul>
	<li><b>For loops</b></li>
</ul>

__Examples__

* range function provides list of numbers to the number specified

```python
	for count in range(5) :
		print(count)
```
* range c=function also have multiple input (start_number, end_number, interval)

```python
	for count in range(10,20,2) :
		print(count)
```

* looping through a list 

```python
	item_list = [2,3,55,5,44,2343,54,576]
	
	print(len(item_list)) ## provides the number of items in a list. Example above :- output : n-1

	for value in item_list :
		print(item_list);

