class Difference:
    def __init__(self, a):
        self.__elements = a
        Difference.maximumDifference = 0

        # Add your code here
    def computeDifference(self):
        for i in range(0, len(self.__elements) - 1):
            for j in range(i + 1, len(self.__elements)):
                if abs(self.__elements[i] - self.__elements[j]) > Difference.maximumDifference:
                    Difference.maximumDifference = abs(self.__elements[i] - self.__elements[j])

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)