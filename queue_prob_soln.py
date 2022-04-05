# Problem to Solve: Roller Coaster Queue
rcq = ["Jane", "Thomas", "Mark", "Dorothy", "Shannon", "Ken", "Paul", "Polly"]

print("Welcome to the Roller Coaster! You must be THIS high to ride.")
print(f"There are currently {len(rcq)} people in line.") # How many people are in line?
print(rcq)
print()

print("Jane and Thomas get on the roller coaster.")
# How should they be dequeued?
rcq.pop(0)
rcq.pop(0)
print(rcq)
print()

print("Three more people get in line.") 
# How should they be enqueued?
rcq.append("Dan")
rcq.append("John")
print(f"Now there are {len(rcq)} people in line.") # How many people are now in line?
print(rcq)
print()

print("Four people get on the roller coaster.")
# How should they be dequeued?
rcq.pop(0)
rcq.pop(0)
rcq.pop(0)
rcq.pop(0)
print(f"Now there are {len(rcq)} people still in line.") # How many people are now in line?
print(rcq)
print()

print("Thomas enqueues again because the roller coaster was so much fun, but Jane doesn't want to because she vomited after getting off.")
print("I don't think Thomas is getting a second date.")
# How should he be enqueued?
rcq.append("Thomas")
print(rcq)
print()

print("Paul gets on the roller coaster, but Polly chickens out at the last minute.")
# How should they be dequeued?
rcq.pop(0)
rcq.pop(0)
print(f"Now there are {len(rcq)} people in line.") # How many people are now in line?
print(rcq)
print()

print("Suddenly, a thunder storm breaks out and the theme park must close unexpectedly.")
print("The last four people in line must dequeue without getting a ride on the roller coaster.")
# How should they be dequeued?
rcq.pop(0)
rcq.pop(0)
rcq.pop(0)
rcq.pop(0)
print(f"Hopefully, Paul got off safely. Now there are {len(rcq)} people in line.") # How many people are now in line?
print(rcq)
