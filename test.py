from creational_patterns.singleton_threading import Singleton, test_singleton


if __name__ == '__main__':
    test_singleton('First')

    singleton = Singleton('Second')
    print(singleton.value)
