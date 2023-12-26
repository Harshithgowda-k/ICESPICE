import pickle


with open("login.dat","wb") as f:
    print("clear")
f.close()
'''


 
 



with open ("login.dat","rb") as f:
    try:
        while True:
            s = pickle.load(f)
            for i in s:
                print(s)
                break
    except:
        print("gonnerrr")'''
                       
                        
