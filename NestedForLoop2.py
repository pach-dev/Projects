This is an Inverted Pyramid

for i in range (0,7):# Displays Rows
        
        for j in range(7+i-7):# Displays Columns printing space and reducing themm by 1 and i can redue the space subtrating any figure
                print(" ", end="")# prints spaces in the inner loop
        for k in range(0, 10-i*2+1):#loops the zeros while incrementing it and multiplication & addition to get odd numbers.
                print("0", end="")#prints zeros running on the innerloop

        print(" ")#prints spacing in NEW Lines in between each iteration as per the inner loops      
                
