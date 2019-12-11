import datetime

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

# Define distance between cameras in meters
camera_distance = 300 

##############################
# Read & Parse Data          #
##############################

data_1 = open("C:/Users/Ping/Desktop/bela-final/data_1.txt", "r").read()
data_2 = open("C:/Users/Ping/Desktop/bela-final/data_2.txt", "r").read()

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
    
    # Parse time strings into datetime objects
    entry_2_time = datetime.datetime.strptime(entry.time, '%Y-%m-%dT%H:%M:%S')
    entry_1_time = datetime.datetime.strptime(entries_1[index].time, '%Y-%m-%dT%H:%M:%S')

    # Calculate time difference and convert it to seconds
    time_dif = (entry_2_time - entry_1_time).total_seconds()

    # Calculate average velocity in m/s and convert it to km/h
    avg_velocity = (camera_distance / time_dif) * 3.6

    print("Required time to pass from Camera A to Camera B for vehicle " + entry._id + " is ~" + str(time_dif) + " sec with average speed of " + str(avg_velocity) + " km/h")