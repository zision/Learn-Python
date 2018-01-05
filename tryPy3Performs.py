import time
def isPrime(i):
    for test in range(2,i):
        if i % test == 0:
            return False
    return True

if __name__ == '__main__':
    t1 = time.clock()

    n_loops = 50000
    n_primes = 0

    for i in range(0,n_loops):
        if isPrime(i):
            n_primes += 1

    t2 = time.clock()
    print(str(n_primes))
    print("使用Python3.6执行本计算的时间为%f s" % (t2 - t1))

#使用Numba加速
from numba import jit

@jit
def isPrime(j):
    for test in range(2,j):
        if j % test == 0:
            return False
    return True
@jit
def tp():

    m_loops = 50000
    m_primes = 0

    for j in range(0,m_loops):
        if isPrime(j):
            m_primes += 1
    return m_primes

if __name__ == '__main__':
    t3 = time.clock()
    m_primes = tp()
    t4 = time.clock()

    print(str(m_primes))

    print("使用Number加速执行本计算的时间为:%f s" % (t4 - t3))
