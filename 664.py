class Solution:
    def strangePrinter(self, s: str) -> int:
        dicc = {}
        for i in range(len(s)-1):

            if s[i] != s[i+1]:
                try:
                    dicc[s[i]] += 1
                except:
                    dicc[s[i]] = 1

        try:
            dicc[s[-1]] += 1
        except:
            dicc[s[-1]] = 1
        print(dicc)
        sum_values = sum(value for value in dicc.values())

        sum_values -= max(dicc.values())

        return sum_values + 1
