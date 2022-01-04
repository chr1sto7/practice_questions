"""Have the function BracketCombinations(num) read num which will be an integer greater than or equal to zero,
and return the number of valid combinations that can be formed with num pairs of parentheses.
For example, if the input is 3, then the possible combinations of 3 pairs of parenthesis,
namely: ()()(), are ()()(), ()(()), (())(), ((())), and (()()).
There are 5 total combinations when the input is 3, so your program should return 5."""

import copy
import sys


def bracket_calculator(num: int, output=None):
    if output is None:
        output = []
    iter_count = num * 2
    if len(output) == 0:
        output.append(['(', num - 1, num])
        return bracket_calculator(num, output)

    else:
        recur = 0
        recur_count = 0
        while recur_count < len(output):
            if (output[recur_count][2] == output[recur_count][1]) and (output[recur_count][2] > 0 and output[recur_count][1] > 0):
                recur += 1
                output[recur_count][0] = output[recur_count][0] + '('
                output[recur_count][1] = output[recur_count][1] - 1
                recur_count += 1

            elif output[recur_count][1] > 0 and output[recur_count][2] > 0:
                recur += 1
                line_copy = copy.deepcopy(output[recur_count])
                output[recur_count][0] = output[recur_count][0] + '('
                output[recur_count][1] = output[recur_count][1] - 1
                output.append([line_copy[0] + ')', line_copy[1], line_copy[2] - 1])
                recur_count += 1

            elif output[recur_count][1] == 0 and output[recur_count][2] > 0:
                recur += 1
                output[recur_count][0] = output[recur_count][0] + str(output[recur_count][2] * ')')
                output[recur_count][2] = 0
                recur_count += 1

            elif len(output[recur_count]) > iter_count:
                print('ERROR')
                sys.exit()

            else:
                recur_count += 1
                pass

        if recur > 0:
            return bracket_calculator(num, output)

        else:
            return output


def BracketCombinations(num: int):
    # code goes here

    if num >= 0:
        if num == 0 or num == 1:
            return 1

        else:
            out = bracket_calculator(num)
            return len(out)

    else:
        print('Please pass a valid integer')


# keep this function call here
print(BracketCombinations(3))


