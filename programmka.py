from os import *


def input_n():
  pass


def dictionary(n):
  for i in listdir(n):
        if path.isdir(n + "\\" + i):
            dictionary(n + '\\' + i)
        elif path.isfile(n + '\\' + i):
            name = n + "\\" + i
            size = stat(n + "\\" + i).st_size
            d1[name] = size
    return d1


def duplicate():
  pass


def duplicate_2():
  pass


if __name__ == '__main__':
  d1 = dict() # словарь для записи значений
