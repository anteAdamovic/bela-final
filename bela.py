class Entry :
  def __init__(self, _id, time):
    self._id = _id
    self.time = time

  def __eq__(self, other):
    return self._id == other._id

  def __str__(self):
    return self._id + " " + self.time

  def __hash__(self):
      return id(self._id)

##############################
# Read & Parse Data          #
##############################

data_1 = open("C:/Users/Ping/Desktop/data_1.txt", "r").read()
data_2 = open("C:/Users/Ping/Desktop/data_2.txt", "r").read()

# list(set()) - filters out duplicate entries by converting a list 
# into a set (which has unique entries) and then back into a list
entries_1 = list(set(map(
  lambda e: Entry(e[0], e[1]), map(
    lambda r: r.split(';'), data_1.split('\n')
  )
)))

print("Entries 1:")
for entry in entries_1:
    print(entry)

entries_2 = list(set(map(
  lambda e: Entry(e[0], e[1]), map(
    lambda r: r.split(';'), data_2.split('\n')
  )
)))

print("Entries 2:")
for entry in entries_2:
    print(entry)

##############################
# Data Comparison            #
##############################

# Search entries_2 and find coresponding entries from entries_1
# then compare their times
for entry in entries_2:
    index = entries_1.index(entry)
    print("Found entry " + entry._id + " on index " + str(index))
    
