
names_set = set()


names_set.add('Alice')
names_set.add('Bob')
names_set.add('Charlie')
names_set.add('David')
names_set.add('Eve')


names_set.remove('Bob')
names_set.add('Bobby')
names_set.remove('Alice')
names_set.remove('David')


print("Updated Names Set:", names_set)
