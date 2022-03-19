
# Introduction

If you are from the United States of America, you may not be familiar with the word "queue." In British English, a "queue" is what Americans would call a "line," most commonly one that you wait in. An everyday example of a queue is one that you wait in at the grocery store before checking out. The first person who entered the queue is the first to leave, and the person at the end is the last to check out. The beginning of the line is called the "front," and the end of the line is called the "back." This procedure uses the acronym "FIFO," or, "First In, First Out." The purpose of a queue is to process a collection of requests in a fair and orderly way.

# Two Common Types of Queues

## Web Server Queue

A web server uses a queue in order to keep track of requests as they come in. 

## Reader/Writer Queue

# Queues in Python

In Python, a queue can be represented as a list. In order to enqueue a value to a list, or in layman's terms, add to the back of the list, use the .append() method. 

my_queue.append(value)

Removing a value from a list, or dequeueing it, has two approaches. The first is to remove and return the item from the front of the queue. The second is to pop off index zero.

value = my_queue[0]
del my_queue[0]
or
value = my_queue.pop(0)



# Example

# Problem to Solve

