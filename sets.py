#set methods
#add()
numbers={21,23,34,45}
print("initial set:",numbers)
numbers.add(43)
print("updated set:",numbers)

#remove()
numbers={21,23,34,45}
print("initial set:",numbers)
numbers.remove(23)
print("set after remove:",numbers)

#discard()
numbers={21,23,34,45}
print("initial set:",numbers)
numbers.discard(46)
print("set after discard:",numbers)

#pop()
numbers={23,34,56,78}
print("initial set:",numbers)
numbers.pop()
print("set after pop:",numbers)

#clear()
numbers={45,5,67,89}
print("initial set:",numbers)
numbers.clear()
print("set after clear:",numbers)

#union()
set1={23,34,45,67,7}
set2={23,45,34,67}
print(set1.union(set2))

#intersection
set1={45,56,67,78}
set2={34,56,98}
print(set2.intersection(set1))

#difference
set1={45,56,67,78}
set2={34,56,78,82}
print(set2.difference(set1))

#symmetric difference
set1={2,3,4,5,6}
set2={3,4,5,6,7}
print(set1.symmetric_difference(set2))

#frozenset method
#disjoint()
new=frozenset([1,2,3,4])
new1=frozenset([5,6,7,8])
print(new.isdisjoint(new1))

#issubset()
new=frozenset([1,2,3,4])
new1=frozenset([1,2,3,4,5,6])
print(new.issubset(new1))

#issuperset()
new=frozenset([1,2,3,4])
new1=frozenset([5,6,7,8])
print(new.issuperset(new1))
               
#take a set of no,take elements from user,remove the element from existing set and store in new set
number={1,2,3,4,5,6}
res=set()
num=int(input("enter a number to remove"))
if num in number:   
        number.remove(num)
        res.add(num)
print("removed elements",res)

#research tpoic:
#check whether the below methods are working for set or not i.e issubset(),issuperset(),isdisjoint()
#yes,the methods issubset(),issuperset(),isdisjoint() do work for pythons
a={1,2,3,4,5}
b={1,2,4,5,7,9}
print(a.isdisjoint(b))
print(b.issuperset(a))
print(a.issubset(b))

    