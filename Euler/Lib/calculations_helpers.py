#problem 2
def find_sum_even_fibonacci_numbers(max_num):
    fibonacci_list = [1, 2]
    i = 0
    while True:
        i = i + 1
        fibonacci_one_back = fibonacci_list[i - 1]
        fibonacci_two_back = fibonacci_list[i]
        fibonacci_next = fibonacci_one_back + fibonacci_two_back
        fibonacci_max = max(fibonacci_list)
        if fibonacci_next > max_num:
            break
        else:
            fibonacci_list.append(fibonacci_next)

    fibonacci_list_even_filter = filter(lambda x: x % 2 == 0, fibonacci_list)

    fibonacci_list_even = list(fibonacci_list_even_filter)

    fibonacci_sum = sum(fibonacci_list_even)

    return fibonacci_sum



#problem 3
def calculate_max_prime_factor(n):
    import math
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            max_prime_factor = i
            n = n / i

    return int(max_prime_factor)



#problem 4
def is_palindrome(n):
    num_chars = [int(d) for d in str(n)]
    num_chars_reversed = num_chars[::-1]
    result = num_chars == num_chars_reversed

    return result

def find_largest_palindrome_product(max_number_digits):
    palindrome_array = []
    start_array = []
    for i in range(max_number_digits):
        start_array.append("9")
        start_int = int(''.join(start_array))
     
    max_option = start_int * start_int
    if is_palindrome(max_option):
        palindrome_array.append(max_option)
    else:
        for i in range(start_int):
            for j in range(start_int - 1):
                current_option = i*j
                if is_palindrome(current_option):
                    palindrome_array.append(current_option)
                else:
                    pass
    palindrome = max(palindrome_array)    
    return palindrome



#problem 5
def divisor_list_trimmer(start, end):
    unique_divisor_master = list(range(end, start, -1))
    for i in range(end, start, -1):
        for j in range(i - 1, start, -1):
            if i % j == 0:
                if j in unique_divisor_master:
                    unique_divisor_master.remove(j)
                else:
                    pass

    return unique_divisor_master

def modulo_0_iterator(num, iteration_seq):
    for i in iteration_seq:
        if num % i == 0:
            pass
        else:
            return False

    return True

def find_smallest_multiple(start, end):
    iteration_seq = divisor_list_trimmer(start, end)
    i = 0
    checker = False
    while not checker:
        i += 20
        checker = modulo_0_iterator(i, iteration_seq)

    return i


#problem 6
def calculate_sum_square_difference(start,end):
    import numpy as np
    numbers = list(range(start,end+1))
    numbers_squared = np.square(numbers)
    sum_of_squares = sum(numbers_squared)
    square_of_sums = np.square(sum(numbers))
    result = np.abs(sum_of_squares - square_of_sums)

    return result



#problem 7
def is_prime(num):
    divisor_options = range(2, int(num ** .5) + 1)
    for i in divisor_options:
        if num % i == 0:
            return False
        else:
            pass
    return True


def find_nth_prime(n):
    i = 2
    prime_list = []
    prime_count = len(prime_list)
    while prime_count < n:
        prime = is_prime(i)
        if prime:
            prime_list.append(i)
            prime_count = len(prime_list)
            i += 1
        else:
            i += 1

    nth_prime = max(prime_list)
    return nth_prime



#problem 8
def find_largest_product_in_series(series, char_count):
    import numpy as np
    num = series
    num_str = str(num)
    num_length = len(num_str)
    prod = 0
    for i in range(0, num_length - (char_count - 1)):
        num_list = []
        for n in range(0, char_count):
            num_list.append(int(num_str[(n + i)]))
            prod_new = np.prod(num_list)
            if prod_new > prod:
                prod = prod_new
            else:
                pass

    return prod



#problem 9
def find_pythagorean_triplet_product(n):
    import numpy as np
    triplet_list = []
    for a in range(1, int(n / 3) + 1):
        for b in range(a + 1, int(n / 2) + 1):
            c = n - a - b
            c_sqr = c * c
            b_sqr = b * b
            a_sqr = a * a
            if (a_sqr + b_sqr == c_sqr):
                triplet_list = [a, b, c]
                triplet_prod = np.prod(triplet_list)

    return triplet_prod



#problem 10
#this calls a previously defined function: is_prime
def find_sum_of_primes_below(n):
    prime_list = []
    for i in range(2, n + 1):
        if is_prime(i):
            prime_list.append(i)
        else:
            pass

    result = sum(prime_list)

    return result



#problem 11
def find_largest_product_in_grid(adjacents, grid_rows, grid_columns, grid_text):
    import numpy as np
    array = np.array([int(x) for x in grid_text.split()]).reshape(grid_rows, grid_columns)
    inverted_array = array[::-1, ]
    largest_product = 0
    for i in range(0, grid_rows):
        for j in range(0, grid_columns):
            row_prod = np.prod(array[i][j:j + adjacents])
            col_prod = np.prod(array[:, j][i:i + adjacents])
            rdiag_prod = np.prod(np.diagonal(array, j - i)[j:j + adjacents])
            ldiag_prod = np.prod(np.diagonal(inverted_array, j - i)[j:j + adjacents])
            largest_product = max(largest_product, row_prod, col_prod, rdiag_prod, ldiag_prod)

    return largest_product


