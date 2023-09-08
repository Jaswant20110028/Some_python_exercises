# First tell the Program that you want to code or decode the message
a=int(input("Press 1 for Coding and Press 2 for Decoding: "))

# a can be either 1 or 2 otherwise raise an error
if not (a==1 or a==2):
    raise ValueError("The input Could be either 1 for coding or 2 for decoding")

# For coding take message as input you want to code
if a==1:
    m=input("Message: ")
    
    # We will split the string using space
    k=m.split(" ") #it is in list as each word of string

    v=[]

    for i in k:
        if len(i)<=3:
            c=i[::-1] #just will be tsuj
        else:
            c="hjk"+i[1:]+i[0]+"bvs"
        
        v.append(c)
    
    b=(" ".join(v))
    print("Coded Message: ",b)

# Decoding The messages
if a==2: 
    m=input("Coded Message: ")
    
    # We will split the string using space
    k=m.split(" ") #it is in list as each word of string

    v=[]

    for i in k:
        if len(i)<=3:
            c=i[::-1] #just will be tsuj
        else:
            c=i[-4]+i[3:-4]
        
        v.append(c)
    
    b=(" ".join(v))
    print("Decoded Message: ",b)



    