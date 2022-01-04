"""Have the function HistogramArea(arr) read the array of non-negative integers stored in arr which will represent the heights of bars on a graph (where each bar width is 1), and determine the largest area underneath the entire bar graph. For example: if arr is [2, 1, 3, 4, 1] then this looks like the following bar graph:

Examples
Input: [6, 3, 1, 4, 12, 4]
Output: 12
Input: [5, 6, 7, 4, 1]
Output: 16"""


def histogram_helper(arr: list):
    if len(arr) == 1:
        return arr[0]

    else:
        recur_len = len(arr)
        start_index = 0
        largest_area = 0
        # iterate through lists and calc iif new area is larger or smaller than previous
        while start_index < recur_len:
            out_arr = []
            current_loop_max = 0
            for i in range(start_index, recur_len):
                if len(out_arr) == 0:
                    out_arr.append(arr[i])
                    current_loop_max += arr[i]

                elif arr[i] >= arr[i-1]:
                    out_arr.append(arr[i])
                    current_loop_max = out_arr[0] * len(out_arr)

                else:
                    out_arr.append(arr[i])
                    total = arr[i] * len(out_arr)

                    if total >= current_loop_max:
                        current_loop_max = 0
                        current_loop_max += total
                    else:
                        break

            start_index += 1

            if current_loop_max > largest_area:
                largest_area = 0
                largest_area += current_loop_max

        return largest_area


def HistogramArea(arr):
    # code goes here
    out = histogram_helper(arr)
    return out


# keep this function call here
print(HistogramArea([5, 6, 7, 4, 1]))
