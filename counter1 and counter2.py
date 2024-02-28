counter1 = 100
counter2 = -100

while counter1 != counter2:
    counter1 -= 1
    counter2 += 1
    counter1_str = "Counter 1: " + str(counter1)
    counter2_str = "Counter 2: " +str(counter2)
    if counter1 == counter2:
        print("YOUR COUNTERS ARE EQUAL NOW ARE YOU HAPPY!!!???")
        
    else:
        print(counter1_str + " " + counter2_str)