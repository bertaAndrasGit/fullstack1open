def add(x,y):
    return x+y

def double(x):
    return x*2


def main():
    print(add(5,5))

    #el lehet nevezni
    add2 = lambda x,y: x+y
    print(add2(5,5))

    #vaqy így is lehet csinálni
    print((lambda x, y: x + y)(5,5))



    sequence = [1,2,3,4,5]

    doubled = map(double,sequence)
    print(list(doubled))

    #a map ezt csinálja
    print([double(x) for x in sequence])

    #vagy így is lehet
    doubled2 = list(map(lambda x: x*2,sequence))
    print(doubled2)

if __name__ == '__main__':
    main()