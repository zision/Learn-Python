#coding=utf-8
import sys


def findkn(l, k):
    newl = [i + k for i in l]
    return len(set(l) & set(newl))


if __name__ == '__main__':
    n = list(sys.stdin.readline().strip())
    k = int(n[1])
    l = list(map(int, list(sys.stdin.readline().strip())))
    print int(findkn(l, k))
