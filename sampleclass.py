class MysamplClass:
    def Hello(self,n):  # self can be any local name

        self.name=n  #name is insde the object
    def print_name(self):
        print(self.name)


x = MysamplClass()
y = MysamplClass()

#x.Hello()    # object oriented calling

#MysamplClass.Hello(x)  #this way also we can call method

name = "Pooja"
x.Hello(name)
y.Hello("Pooja P Suku")
x.print_name()
y.print_name()