def myFunc(list):
    if len(list) > 1:
        for i in range(len(list) - 1):
            print(list[i] + ', ', end='')
        print('and ' + list[-1])
    elif len(list) == 1:
        for i in range(len(list)):
            print(list[i])
    else:
        print('Empty list')

list1 = ['apples', 'bananas', 'tofu', 'cats']
list2 = ['apples']
list3 = []
myFunc(list1)