import copy


def min_str_recurser(target_string: str, chars_dict: dict):
    recur = 0
    total_recur = len(target_string)
    char_len = len(chars_dict)
    smallest_substring = copy.deepcopy(target_string)

    # iterate through word starting from different point each time
    # if len of chars_dict == inner_smallest_sub, break for loop
    while total_recur - recur >= char_len:
        inner_smallest_sub = ''
        test_dict = {}
        loop_chars = copy.deepcopy(chars_dict)

        for i in range(recur, total_recur):
            try:
                if loop_chars[target_string[i]] > 0:
                    loop_chars[target_string[i]] = loop_chars[target_string[i]] - 1
                    inner_smallest_sub += target_string[i]
                    if target_string[i] in test_dict:
                        test_dict[target_string[i]] += 1

                    else:
                        test_dict[target_string[i]] = 1

                    if test_dict == chars_dict:
                        break

                else:
                    inner_smallest_sub += target_string[i]

            except KeyError:
                inner_smallest_sub += target_string[i]

        if test_dict == chars_dict:

            if len(inner_smallest_sub) < len(smallest_substring):
                smallest_substring = copy.deepcopy(inner_smallest_sub)

        recur += 1

    return smallest_substring


def MinWindowSubstring(strArr):
    word = strArr[0]
    chars = {}
    for i in strArr[1]:
        if i in chars:
            chars[i] += 1

        else:
            chars[i] = 1

    minimum_substring = min_str_recurser(word, chars)
    return minimum_substring


# keep this function call here
print(MinWindowSubstring(["ahffaksfajeeubsne", "jefaa"]))

