from BloomFilter import BloomFilter
import random
import string
from itertools import product

def generateEmail():
    body = "".join(random.choices(string.ascii_lowercase + string.digits, k = 10))
    domains = ["gmail.com", "yahoo.com", "outlook.com"]

    return body + random.choice(domains)

def testFalsePositive(m, k, s, e):
    bloom = BloomFilter(size=m, hashCount=k)

    spams = [generateEmail() for i in range(s)]
    for spam in spams:
        bloom.add(spam)
    
    emails = [generateEmail() for i in range(e)]

    falsePositive = sum(1 for email in emails if bloom.check(email))
    print(f"{falsePositive}, {m}, {k}, {s}, {e}")

mValues = [10, 250, 500]
kValues = [3, 6, 9]
spamsValues = [50, 180, 350]
emailsValues = [200, 500, 1000]

for m, k, s, e in product(mValues, kValues, spamsValues, emailsValues):
    testFalsePositive(m, k, s, e)