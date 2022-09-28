"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = [2]
    count = 2
    for number in range(1, number_of_primes):
        while len(list) <= number:
            count += 1
            status = False
            for prime in list:
                if count % prime == 0:
                    status = True
                    break
                else:
                    continue
            if status:
                continue
            else:
                list.append(count)
                break

    return list
