#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def counthats(count,am_cats):
    allcats=[]
    if count<=am_cats:
        for roun in range(1,count+1):
            for cats in range(1,am_cats+1):

                if cats%roun==0:
                    if cats not in allcats:
                        allcats.append(cats)
                    else:
                        allcats.remove(cats)
                    m=print(f"These cats are with {allcats}",len(allcats))
    else:
        print("Rounds are greater than cats")
        m=print("Nothing") 
        
    return m


while True:
    
    ask=input("Do you wanr to start: y/n ")
    if not ask.lower()=="y":
        break
    
    try:
        count_rounds=int(input("How many rounds: "))
        count_cats=int(input(("How many cats: ")))
    
    except ValueError:
        print("Try one more time!")
    counthats(count_rounds,count_cats)

    
    


# In[ ]:





# In[ ]:




