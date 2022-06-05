import concurrent.futures


def factorize_for_process(number):
    dividers = [1]
    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            dividers.append(i)
    dividers.append(number)
    return dividers


def factorize(*numbers):
    with concurrent.futures.ProcessPoolExecutor(5) as ex:
        all_dividers = ex.map(factorize_for_process, numbers)
    return all_dividers


if __name__ == '__main__':
    a, b, c, d = factorize(128, 255, 99999, 10651060)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]

    print(a)
    print(b)
    print(c)
    print(d)
