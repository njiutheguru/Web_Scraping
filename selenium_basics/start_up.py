# Starting up with selenium
# inspecting id
# collection modules..
# subclasses of the dictionary..
# 1. The counter container - keeps the number of elements in an iterable 
from collections import Counter

count = Counter(['B','B','r','A','A','A','A','B'])
print(count)
list1= ['A','A','A','B']
count.update(list1)
print(count)

# OrderedDict  remembers the order in which values were added
from collections import OrderedDict
d = {}
d['a'] = 5
d['b'] = 3
d['c'] = 55
d['d'] = -88
print(d)
d.pop('a')
print(d)
d['a']=8899
print(d)

# default dict # a subclass to the dicionary...
from collections import defaultdict
dd = defaultdict(int)# datatype integer passed means that the values will be of type integer
nums = [1,2,3,4,5,66,4,3,4,3,2]
for i in nums:
    dd[i] += 1

print(dd) # returns the number of occurrences for each keys..
dd2 = defaultdict(list)

for i in nums:
    dd2[i].append(i)

print(dd2)
print(dd2[99])

# chain map container in python...
from collections import ChainMap
d1 = {'a':1, 'b':2}
d2 = {'c':3, 'd':5}
d3 = {'e':4, 'f':6}
c = ChainMap(d1, d2, d3)
print(c)
print(c['a'])
for i in c.keys():
    print(i)
print("============")
for i in c.values():
    print(i)

# Named tuple collection module
# 
my_tuple =('Dave', 'London', 22)
print("Lives in : ",my_tuple[1])

from collections import namedtuple
# age=0
# height =0
employee = namedtuple("employ",['name', 'age', 'height'])
emp1 = employee('Stephen', 79, 6.77)
print(emp1.name)

# Deque container
from collections import deque
de = deque([1,2,3,4])
print("Appending 4 to the right...", de)
de.appendleft(6)
print("Appending 6 to the left...",de)

de.pop() # deletes from the right side of the list..
print("Deleting method from the right", de)

de.popleft()
print("Deleting element from the left...", de)
