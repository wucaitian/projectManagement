def test(func):
    def abc():
        func()
        print('abc')
    return abc

@test
def ttt():
    print('ttt')


ttt()
