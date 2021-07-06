def countEvenOdd(n):
     
    even_count = 0
    odd_count = 0
    while (n > 0):
        rem = n % 10
        if (rem % 2 == 0):
            even_count += 1
        else:
            odd_count += 1
             
        n = int(n / 10)
     
    print( "Even count : " , even_count)
    print("\nOdd count : " , odd_count)
    if (even_count % 2 == 0 and
                    odd_count % 2 != 0):
      if(even_count > odd_count):
        print("Even numbers are higher than Odd numbers")
        return 1
    else:
        return 0
    if(even_count > odd_count):
        print("Even numbers are higher than Odd numbers")
    elif(odd_count > even_count):
         print("Odd numbers are higher than Evend numbers")
    else:
           print("they are equal")
 
# Driver code
n = 44787735451;
t = countEvenOdd(n);
