for i in range(1,100):
    if i%5==0 and i%3==0:
        print('FooBar')
    elif i%3==0:
        print('Foo')
    elif i%5==0:
        print('Bar')
    else:
        print(i)