# Problem 1: Hundred Acre Wood

def welcome():
    print("Welcome to The Hundred Acre Wood!")
welcome()


#Problem 2: Greeting

def greeting(name):
    print("Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")

greetings("Michael")
greetings("Winnie the Pooh")


#Problem 3: Catchphrase

def print_catchphrase(character):
    if character == "Pooh":
        print("Oh bother!")	
    if character == "Tigger":
        print("TTFN: Ta-ta for now!")
    if character == "Eeyore":
        print("Thanks for noticing me.")
    if character == "Christopher Robin":
        print("Silly old bear.")
    else:
        print("Sorry! I don't know {character}'s catchphrase!")

character = "Pooh"
print_catchphrase(character)

character = "Piglet"
print_catchphrase(character)

#Problem 4: Return Item

def get_item(items, x):
    return items[x]

items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
get_item(items, x)

items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
get_item(items, x)


#Problem 5: Total Honey

def sum_honey(hunny_jars):
    sum = 0
    for i in hunny_jars:
        sum += hunny_jars[i]

    return sum

hunny_jars = [2, 3, 4, 5]
sum_honey(hunny_jars)

hunny_jars = []
sum_honey(hunny_jars)

#Problem 6: Double Trouble

def doubled(hunny_jars):
    for i in hunny_jars:
        hunny_jars[i]= i*2

    return hunny_jars

hunny_jars = [1, 2, 3]
doubled(hunny_jars)

#Problem 7: Poohsticks

def count_less_than(race_times, threshold):
    count = 0
    for i in race_times:
        if race_times[i]<threshold:
            count+=1
        else:
            continue
    return count

race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
count_less_than(race_times, threshold)

race_times = []
threshold = 4
count_less_than(race_times, threshold)


Problem 8: Pooh's To Do's
Write a function print_todo_list() that accepts a list of strings named tasks. The function should then number and print each task on a new line using the format:

Pooh's To Dos:
1. Task 1
2. Task 2
...

def print_todo_list(task):
	pass
Example Usage

task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list(task)

task = []
print_todo_list(task)
Example Output:

Pooh's To Dos:
1. Count all the bees in the hive
2. Chase all the clouds from the sky
3. Think
4. Stoutness Exercises

Pooh's To Dos:
✨ AI Hint: range()

Problem 9: Pairs
Rabbit is very particular about his belongings and wants to own an even number of each thing he owns. Write a function can_pair() that accepts a list of integers item_quantities. Return True if each number in item_quantities is even. Return False otherwise.

def can_pair(item_quantities):
	pass
Example Usage

item_quantities = [2, 4, 6, 8]
can_pair(item_quantities)

item_quantities = [1, 2, 3, 4]
can_pair(item_quantities)

item_quantities = []
can_pair(item_quantities)
Example Output:

True
False
True
💡 Remainders with Modulus Division

Problem 10: Split Haycorns
Piglet's has collected a big pile of his favorite food, haycorns, and wants to split them evenly amongst his friends. Write a function split_haycorns() to help Piglet determine the number of ways he can split his haycorns into even groups. split_haycorns() accepts a positive integer quantity as a parameter and returns a list of all divisors of quantity.

def split_haycorns(quantity):
	pass
Example Usage

quantity = 6
split_haycorns(quantity)

quantity = 1
split_haycorns(quantity)
Example Output:

[1, 2, 3, 6]
[1]


Problem 11: T-I-Double Guh-ER
Signs in the Hundred Acre Wood have been losing letters as Tigger bounces around stealing any letters he needs to spell out his name. Write a function tiggerfy() that accepts a string s, and returns a new string with the letters t, i, g, e, and r from it.

def tiggerfy(s):
	pass
Example Usage

s = "suspicerous"
tiggerfy(s)

s = "Trigger"
tiggerfy(s)

s = "Hunny"
tiggerfy(s)
Example Output:

"suspcous"
""
"Hunny"
💡Hint: String Methods

Problem 12: Thistle Hunt
Pooh, Piglet, and Roo are looking for thistles to gift their friend Eeyore. Write a function locate_thistles() that takes in a list of strings items and returns a list of the indices of any elements with value "thistle". The indices in the resulting list should be ordered from least to greatest.

def locate_thistles(items):
	pass
Example Usage

items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
locate_thistles(items)

items = ["book", "bouncy ball", "leaf", "red balloon"]
locate_thistles(items)
Example Output:

[0, 3]
[]