# Count median of input years

#############################

year_amount = 0
sum_year = 0
max_year = 0
min_year = 110
input_year = -1

print("Input a birth year, e.g. 1996. To end, input 0.") 

while input_year != 0: 
    input_year = int(input("Input year: "))
    alder = 2020 - input_year  

    if alder < 0 or alder > 110 and alder != 2020:  
      print("Not accepted, try again.")            
    else:
      if input_year > 0:
        year_amount = year_amount + 1       
        sum_year = sum_year + alder
        if alder < min_year:
          min_year = alder
        if alder > max_year:
          max_year = alder

print("Median age is ", sum_year / year_amount, "years.")     
print("Youngest is ", min_year, " and oldest is ", max_year)     