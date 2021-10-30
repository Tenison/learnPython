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

__Lists__

```python
	item_list = [2,3,55,5,44,2343,54,576]
	
	## below provides the lenght of the list. Example :- output : n-1
	print(len(item_list))
```

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

```python
	item_list = [2,3,55,5,44,2343,54,576]

	for value in range(len(item_list)) :
		print(value);
```
