import hashlib
from bitarray import bitarray

class BloomFilter:
    def __init__(self, size = 10, hashCount = 3):
        self.size = size # m
        self.hashCount = hashCount #k
        self.bitArray = bitarray(size)
        self.bitArray.setall(0)

    def hashFunc(self, value):
        positions = []
        for i in range(self.hashCount):
            hashValue = hashlib.sha256(f"{value}{i}".encode()).hexdigest()
            positions.append(int(hashValue, 16) % self.size)
        return positions

    def add(self, item):
        for pos in self.hashFunc(item):
            self.bitArray[pos] = 1

    def check(self, item):
        return all(self.bitArray[pos] for pos in self.hashFunc(item))