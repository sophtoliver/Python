# Sophia M. Toliver, CIS 345 T TH 10:30, A5

class Employee:
    """Adds an employee to the database. An Employee can also be a Manager."""
    def __init__(self, name='', eid=''):
        self.name = name
        self.eid = eid

    @property
    def name(self):
        return self.__name.capitalize()

    @name.setter
    def name(self,  new):
        if new.isalpha():
            self.__name = new
        else:
            self.__name = 'Unknown'

    @property
    def eid(self):
        return self.__eid.zfill(4)

    @eid.setter
    def eid(self, new):
        if len(new) == 0:
            self.__eid = '9999'
        else:
            self.__eid = new

    def __str__(self):
        return f'{self.eid}: {self.name}'


class Manager(Employee):
    """Records what Employees are under each Manager's supervision"""
    def __init__(self, name='', eid='', subordinates=None):
        super().__init__(name)
        super().__init__(eid)
        if subordinates is None:
            self.subordinates = []

    def print_subordinates(self):
        """Prints what Employees are subordinates of the given Manager"""
        print(f"\t{self.name}'s Employees")
        for sub in self.subordinates:
            print(f'\t{sub}')

    def add_subordinate(self):
        """Adds subordinates to each Manager"""
        amount = int(input('How many subordinates? '))
        for x in range(amount):
            name = input('Enter subordinate name: ')
            eid = input('Enter subordinate ID: ')
            subordinate = Employee(name, eid)
            self.subordinates.append(subordinate)


def main():
    """Shows welcome message, asks user to enter Employees to database, and prints all that was given"""
    employee_roster = []
    print("{:^50}".format('Employee Management System'))
    print()
    print('Adding Employees...')
    print()
    more = 'y'
    while more == 'y':
        employee_roster.append(add_employee())
        more = input('Do you want to enter more? ').casefold()
        print()

    print('Printing Employee List')
    for employee in employee_roster:
        print(employee)
        if isinstance(employee, Manager):
            Manager.print_subordinates(employee)


def add_employee():
    """Adds Employees to the database and specifies who is a Manager"""
    name = input('Enter name: ')
    eid = input('Enter ID: ')
    manager = input('Is the employee a manager? (Y/N) ').casefold()
    if manager == 'y':
        new = Manager()
        new.add_subordinate()
    else:
        new = Employee()

    new.name = name
    new.eid = eid
    return new


if __name__ == '__main__':
    main()





