import time, sys
indent = 0 # spaces to indent
indentIncreasing = True #increasing or not

try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.05) #pause for 1/10 second

        if indentIncreasing:
            indent = indent + 2
            if indent == 50:
                indentIncreasing = False
        
        else:
            indent = indent - 2
            if indent == 0:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()