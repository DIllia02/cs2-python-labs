import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from labs.lab1 import task1, Task2, Task3


def main():
    print(" ДЕМОНСТРАЦІЯ ЛАБОРАТОРНОЇ РОБОТИ №1 \n")

    task1.main()

    Task2.main()

    Task3.main()


if __name__ == "__main__":
    main()
