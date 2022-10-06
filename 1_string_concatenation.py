# string concatenation using mad libs 

#####################################


class main:

    def __init__ (self, color1, color2, food):
        self.color1 = color1
        self.color2 = color2
        self.food = food

madlib_1 = main('red', 'blue', 'burger')
madlub_2 = main('green', 'yellow', 'pasta')


one = ("Roses are " + madlib_1.color1 + ", violets are " + madlib_1.color2 + ", I love " + madlib_1.food)
two = ("Roses are " + madlub_2.color1 + ", violets are " + madlub_2.color2 + ", I love " + madlub_2.food)

print (one)
print (two)

#comment