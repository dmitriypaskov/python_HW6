def not_primes(a, b):
    if a < b <= 20000:
        prost = "2357"
        arr = []
        arr1 = []
        for i in range(a, b):
            j = 0
            app = True
            while j < len(str(i)):
                if str(i)[j] in prost:
                    app = True
                    j += 1
                else:
                    app = False
                    break
            if app:
                arr.append(i)
        for i in arr:
            for j in range(2, i):
                if i != j and i % j == 0:
                    arr1.append(i)
                    break
        return arr1