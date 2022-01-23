class TestClass:
    a = 1
    b = 2

    def donble(self):
        return self.a * 2


bob = TestClass()
tom = TestClass()
tom.a = 2
print(bob.a)
print(tom.a)
