
# Introduction

If you are from the United States of America, you may not be familiar with the word "queue." In British English, a "queue" is what Americans would call a "line," most commonly one that you wait in. An everyday example of a queue is one that you wait in at the grocery store before checking out. The first person who entered the queue is the first to leave, and the person at the end is the last to check out. The beginning of the line is called the "front," and the end of the line is called the "back." This procedure uses the acronym "FIFO," or, "First In, First Out." The purpose of a queue is to process a collection of requests in a fair and orderly way.

# Two Common Types of Queues

## Web Server Queue

A web server uses a queue in order to keep track of requests as they come in. 

## Reader/Writer Queue

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

# Example: Roller Coaster Queue

Roller Coasters are known for having very long lines. We can use the queue data structure in order to simulate how the theme-park-goers interact with it.

``` python
# Roller Coaster Queue
rcq = ["Jane", "Thomas", "Mark", "Dorothy", "Shannon", "Ken", "Paul", "Polly"]

print("Welcome to the Roller Coaster! You must be THIS high to ride.")
print(f"There are currently {len(rcq)} people in line.")
print(rcq)
print()

print("Jane and Thomas get on the roller coaster.")
rcq.pop(0)
rcq.pop(0)
print(rcq)
print()

print("Three more people get in line.")
rcq.append("Caleb")
rcq.append("Mary")
rcq.append("Josh")
print(f"Now there are {len(rcq)} people in line.")
print(rcq)
print()

print("Four people get on the roller coaster.")
rcq.pop(0)
rcq.pop(0)
rcq.pop(0)
rcq.pop(0)
print(f"Now there are {len(rcq)} people still in line.")
print(rcq)
print()

print("Thomas enqueues again because the roller coaster was so much fun, but Jane doesn't because she vomited after getting off.")
print("I don't think Thomas is getting a second date.")
rcq.append("Thomas")
print(rcq)
print()

print("Paul gets on the roller coaster, but Polly chickens out at the last minute.")
rcq.pop(0)
rcq.pop(0)
print(f"Now there are {len(rcq)} people in line.")
print(rcq)
print()

print("Suddenly, a thunder storm breaks out and the theme park must close unexpectedly.")
print("The last four people in line must dequeue without getting a ride on the roller coaster.")
rcq.pop(0)
rcq.pop(0)
rcq.pop(0)
rcq.pop(0)
print(f"Hopefully, Paul got off safely. Now there are {len(rcq)} people in line.")
print(rcq)
```

# Problem to Solve

