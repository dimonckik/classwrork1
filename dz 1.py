class Classmates:
    classroomteacher = "Olena Viktoryvna"
    School = "N83"
    age = "16"

    def __init__(self, name, height, hobby):
        self.name = name
        self.height = height
        self.hobby = hobby




person1 = Classmates(name="Ivan", height="180", hobby="Basketball")
person2 = Classmates(name="Igor", height="173", hobby="Football")
person3 = Classmates(name="Anton", height="168", hobby="Box")

print(person1.name)
print(person2.name)
print(person3.name)




class friends:
    hobby = "swimming"
    city = "Odessa"
    age = "15"

    def __init__(self, name, height, eyes):
        self.name = name
        self.height = height
        self.eyes = eyes



friend1 = friends(name="Nikita", height="175", eyes="Brown")
friend2 = friends(name="Sergey", height="179", eyes="Blue")
friend3 = friends(name="Alex", height="190", eyes="Gray")

print(friend1.name)
print(friend2.name)
print(friend3.name)