import lib.calculation_helpers as ch
import more_helpers as mh


def problem1(divisors, max_num):
    nums = ch.find_nums_divisible_by_divisors(divisors, max_num)
    total = sum(nums)
    return total



problem1([3,5], 1000)
problem2()
