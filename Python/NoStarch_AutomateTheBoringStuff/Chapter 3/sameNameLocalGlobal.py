from pkg_resources import EGG_DIST


def spam():
    global eggs
    eggs = 'spam' #global

def bacon():
    eggs = 'bacon' #local

def ham():
    print(eggs) #global

eggs = 42 #global
spam() #reassigns global
print(eggs)