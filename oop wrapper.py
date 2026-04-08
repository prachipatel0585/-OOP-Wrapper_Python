print('---python oop project:employee management system---')
def mainu():
    print('choose an operation:')
    print('1.create a person')
    print('2. create an employee')
    print('3. create a manager')
    print('4. show details')
    print('5. compare salaries')
    print('6. exit')
mainu()
print(input('enter your choice:'))
print(input('enter name:'))
print(input('enter age:'))
name = 'prachi patel'
age = 22
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show_detailes(self):
        print(f'{self.name} and {self.age}')
a = person(name,age)
print(f'person created with name: {name} and age:{age}')
a.show_detailes()