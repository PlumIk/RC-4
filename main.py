class RC4:
    S = bytearray(256)
    x = 0
    y = 0

    def __init__(self, key):
        key = bytes(key, 'utf-8')
        self.__doS(key)


    def __cust_swap(self, i, j):
        swap = self.S[i]
        self.S[i] = self.S[j]
        self.S[j] = swap

    def __doS(self, key):
        a = len(key)
        for i in range(256):
            self.S[i] = i

        j = 0
        for i in range(256):
            j = (j + self.S[i] + key[i % a]) % 256
            self.__cust_swap(i, j)

    def __p_rand(self):
        self.x = (self.x + 1) % 256
        self.y = (self.y + self.S[self.x]) % 256
        self.__cust_swap(self.x, self.y)
        return self.S[(self.S[self.x] + self.S[self.y]) % 256]

    def do(self, data) -> bytearray:
        data = bytearray(data, 'utf - 8')
        size = len(data)
        ret = bytearray(size)
        for i in range(size):
            ret[i] = data[i] ^ self.__p_rand()
        return ret

    def dont_do(self, data) -> str:
        size = len(data)
        ret = bytearray(size)
        for i in range(size):
            ret[i] = data[i] ^ self.__p_rand()
        return ret.decode()


key = 'trycode'
word = 'word'

while (True):
    word = input()
    print('Input is: ', word)
    work = RC4(key)
    coder = work.do(word)
    work = RC4(key)
    uncoer = work.dont_do(coder)

    print('Code :', coder)
    print('Encode :', uncoer)
