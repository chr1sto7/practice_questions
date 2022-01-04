"""You will be given a list of stock prices for a given day and your goal is to return the maximum profit that
could have been made by buying a stock at the given price and then selling the stock later on.

For example if the input is:

[45, 24, 35, 31, 40, 38, 11]

then your program should return 16 because if you bought the stock at $24 and sold it at $40,
a profit of $16 was made and this is the largest profit that could be made.

If no profit could have been made, return -1."""


def stock_maximum_profit(arr: list):
    """return the maximum possible profit"""
    loop_len = len(arr)
    best_price = 0
    index = 0
    for buy in arr:
        for j in range(index, loop_len):
            new_return = arr[j] - buy
            if new_return > best_price:
                best_price = 0
                best_price += new_return
        index += 1

    if best_price == 0:
        return -1

    else:
        return best_price


if __name__ == '__main__':
    test_1 = (stock_maximum_profit([45, 24, 35, 31, 40, 38, 11]))
    print(f'Best possible profit is ${test_1}')

    print(stock_maximum_profit([9, 8, 7, 6, 5]))
    print(stock_maximum_profit([10]))


