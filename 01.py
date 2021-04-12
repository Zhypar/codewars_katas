class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties
        
    def total(self):
        five = self.fives * 5
        ten = self.tens * 10
        twenty = self.twenties * 20
        total = five + ten + twenty
        return total, self.name



def most_money(students):
    arr = []
    new_arr = []
    for student in students:
        arr.append(student.total())
        
    for i in arr:
        new_arr.append(i[0])
    if (set(new_arr) != new_arr) and (len(set(new_arr)) <= 1) and (len(arr)!=1):
        return "all"
    elif len(arr) == 1:
        return (max(arr)[1])
        
    return (max(arr)[1])
    