
# Introduction to Queues

If you are from the United States of America, you may not be familiar with the word "queue." In British English, a "queue" is what Americans would call a "line," most commonly one that you wait in. An everyday example of a queue is one that you wait in at the grocery store before checking out. The first person who entered the queue is the first to leave, and the person at the end is the last to check out. The beginning of the line is called the "front," and the end of the line is called the "back." This procedure uses the acronym "FIFO," or, "First In, First Out." The purpose of a queue is to process a collection of requests in a fair and orderly way.

# Queues in Python

In Python, a queue can be represented as a list. In order to enqueue a value to a list, or in layman's terms, add to the back of the list, use the .append() method. 

``` python
my_queue.append(value)
```

Removing a value from a list, or dequeueing it, has two approaches. The first is to remove and return the item from the front of the queue. The second is to pop off index zero.

``` python
value = my_queue[0]
del my_queue[0]
or
value = my_queue.pop(0)
```

In order to return the size of a queue, use the length() function.

``` python
length = len(my_queue)
```

You can learn whether a queue is empty, using a boolean if statement, which will return true if the length of the queue is zero.

``` python
if len(my_queue) == 0:
  print("Empty queue!")
```

# Example: Stoplight Queue

A good example of a queue can be found in the line of cars found at a stoplight at the end of a one-way street. We'll start with a queue that already has three vehicles.

``` python
slq = ["red car", "blue car", "black car"]

print("At a stoplight at the end of a one-way road, there are three cars.")
print("Before the light changes to green, a grey truck and another blue car roll up to the end of the line.")
slq.append("grey truck")
slq.append("blue car")

print("The light goes green and the three original cars are able to move through the intersection before the light goes red.")
slq.pop(0)
slq.pop(0)
slq.pop(0)

print("A red truck, a yellow bug, and a green suv join the line.")
slq.append("red truck")
slq.append("yellow bug")
slq.append("green suv")

print("The grey truck turns right.")
slq.pop(0)

print("The light is taking a long time, so four more vehicles join the line.")
slq.append("green jeep")
slq.append("limo")
slq.append("semi")
slq.append("pink suv")

print("The light finally goes red, and five vehicles zoom through.")
slq.pop(0)
slq.pop(0)
slq.pop(0)
slq.pop(0)
slq.pop(0)

print(slq)
print("Printing the queue, we see that three vehicles are left: the limo, the semi, and the pink suv.")
```

# Problem to Solve: Roller Coaster Queue

Roller Coasters are known for having very long lines. Use this code to enqueue and dequeue a line and find out how many people are in the line at a given time.

``` python
rcq = ["Jane", "Thomas", "Mark", "Dorothy", "Shannon", "Ken", "Paul", "Polly"]

print("Welcome to the Roller Coaster! You must be THIS high to ride.")
print(f"There are currently {?} people in line.") # How many people are in line?
print(rcq)
print()

print("Jane and Thomas get on the roller coaster.")
# How should they be dequeued?
print(rcq)
print()

print("Three more people get in line.") 
# How should they be enqueued?
print(f"Now there are {?} people in line.") # How many people are now in line?
print(rcq)
print()

print("Four people get on the roller coaster.")
# How should they be dequeued?
print(f"Now there are {?} people still in line.") # How many people are now in line?
print(rcq)
print()

print("Thomas enqueues again because the roller coaster was so much fun, but Jane doesn't want to because she vomited after getting off.")
print("I don't think Thomas is getting a second date.")
# How should he be enqueued?
print(rcq)
print()

print("Paul gets on the roller coaster, but Polly chickens out at the last minute.")
# How should they be dequeued?
print(f"Now there are {?} people in line.") # How many people are now in line?
print(rcq)
print()

print("Suddenly, a thunder storm breaks out and the theme park must close unexpectedly.")
print("The last four people in line must dequeue without getting a ride on the roller coaster.")
# How should they be dequeued?
print(f"Hopefully, Paul got off safely. Now there are {} people in line.") # How many people are now in line?
print(rcq)
```
[Solution](.py)
[Return to Welcome Page](0-welcome.md)
