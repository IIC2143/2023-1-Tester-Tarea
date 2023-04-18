from private_test_0 import test_0
from private_test_1 import test_1
from private_test_2 import test_2
from private_test_3 import test_3


def main():
    tests = [
        test_0,
        test_1,
        test_2,
        test_3,
    ]

    for i, test in enumerate(tests):
        print(f'Executing private test {i}')
        test()
        print()


if __name__ == '__main__':
    main()
