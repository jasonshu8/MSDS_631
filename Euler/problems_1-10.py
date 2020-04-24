import lib.calculation_helper as ch

def problem1(max_num,divisors):
    nums = find_nums_divisible_by_divisors(max_num,divisors)
    total = sum(set(nums))
    return total

def problem2(start_value,max_value):
    nums = find_fibonacci_sequence(start_value,max_value)
    total = 0
    for i in nums:
        if (i % 2 == 0):
            total += i
    return total

def problem3(input_number):
    factor_range = find_squared_prime_factors(input_number)
    prime_factors = []
    for i in factor_range:
        is_prime_number = check_if_prime_number(i)
        if is_prime_number == True:
            prime_factors.append(i)
    return max(prime_factors)

def problem4(digits):
    max_list_whole_number = 10 ** digits
    min_list_whole_number = 10 ** (digits - 1)
    possible_palindromes = find_all_possible_values_equating_palindrome(min_list_whole_number, max_list_whole_number)
    palindromes = find_palindromes(possible_palindromes, min_list_whole_number, max_list_whole_number)
    largest_palindrome = max(palindromes)
    return (largest_palindrome)

def problem5(start_divisors,end_divisors):
    divisors = [i for i in range (start_divisors,end_divisors+1)]
    number = 1
    number_check = []
    while len(number_check) != 1:
        if all((number % i == 0) for i in divisors):
            number_check.append(1)
        else:
            number += 1
    return number

def problem6(natural_low,natural_high):
    sum_squares = find_sum_of_squares(natural_low,natural_high)
    square_sum = find_square_of_sum(natural_low,natural_high)
    delta_of_squares = square_sum - sum_squares
    return delta_of_squares

def problem7(prime_number_length):
    prime_numbers = find_every_prime_number(prime_number_length)
    prime_number_position_value = max(prime_numbers)
    return prime_number_position_value

def problem8(number,number_of_adjacents):
    products = find_product_of_adjacents(number,number_of_adjacents)
    max_series = max(products.values())
    return max_series

def problem9(input_sum):
    for a in range (1,(input_sum//2)+1):
        for b in range (1,(input_sum//2)+1):
            for c in range (1,(input_sum//2)+1):
                if (a < b) and (b < c) and ((a**2 + b**2) == c**2) and (a + b + c == 1000):
                    abc_product = a*b*c
    return abc_product

def problem10(start_value,input_value):
    primes = []
    for i in range(start_value,input_value):
        if check_if_prime_number(i) is True:
            primes.append(i)
    sum_of_primes = sum(primes)
    return sum_of_primes

insertion_number = int("""
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450""".replace("\n", ""))

problem1(1000,(3,5))
problem2(1,4000000)
problem3(600851475143)
problem4(3)
problem5(1,20)
problem6(1,100)
problem7(10001)
problem8(insertion_number,13)
problem9(1000)
problem10(1,2000000)
