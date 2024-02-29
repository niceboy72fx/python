for num in range(10, 21):    
    for i in range(2, num):  
        if num % i == 0:     
             print ("%d không phải là số nguyên tố." %(num));
             break;          
    else:                    
         print ("%d là số nguyên tố" %(num));