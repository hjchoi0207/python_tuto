class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):
        print("Fly")

eagle = Eagle()
eagle.fly()
