# string concatenation using mad libs 

#####################################


class madlib:

    def __init__ (self, color1, color2, food):
        self.color1 = color1
        self.color2 = color2
        self.food = food

madlib_1 = madlib('red', 'blue', 'burger')
madlub_2 = madlib('green', 'yellow', 'pasta')


print("Roses are " + madlib_1.color1 + ", violets are " + madlib_1.color2 + ", I love " + madlib_1.food)
print("Roses are " + madlub_2.color1 + ", violets are " + madlub_2.color2 + ", I love " + madlub_2.food)
