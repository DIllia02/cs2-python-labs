import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from labs.lab1 import task1, Task2, Task3


def main():
    print(" ДЕМОНСТРАЦІЯ ЛАБОРАТОРНОЇ РОБОТИ №1 \n")

    print("\n Завдання 1")
    task1.main()

    print("\n Завдання 2")
    Task2.main()

    print("\n Завдання 3")
    Task3.main()


if __name__ == "__main__":
    main()
