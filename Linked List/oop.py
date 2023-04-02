class Boss:
    def __init__(self):
        self.boss = "Isfak Ahmed"
    
    def print_BossName(self):
        print(self.boss)

    def print_BossAge(self, age):
        print("Age: ", age)

obj = Boss()
obj.print_BossName()
obj.print_BossAge(20)