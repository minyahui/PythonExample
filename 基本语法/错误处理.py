
def test(i):
    try:
        print('try...')
        r = 10 / i
        print('result:', r)
    except ZeroDivisionError as e:
        print('except:', e)
    except ValueError as e:
        print('except:', e)
    except BaseException as e:
        print('except',e)
    finally:
        print('finally...')
    print('END')

test(1)
test(0)
test('a')