"""
This is an implementation of KMP algorithm for find all the sub-string that contain the given pattern as a quick revision.
The time complexity of this algorithm is O(m + n), m is the pattern size and n is the input text size
"""

Text = input("Please input the text for searching: ")
Pattern = input("Please input the pattern for searching:")
m = len(Pattern)
next_list = [None] * m


# O(m)
def next_table():
    # init
    next_list[0] = -1
    k = -1
    q = 1
    while q <= m - 1:
        while k >= 0 and Pattern[k + 1] != Pattern[q]:
            k = next_list[k]
        if Pattern[k + 1] == Pattern[q]:
            k = k + 1
        next_list[q] = k
        q = q + 1

    print("\nNext table for given pattern:\n", next_list, "\n")


next_table()


# O(n)
def kmp_algorithm():
    count = 0
    q = -1
    for i in range(len(Text)):
        while q >= 0 and Pattern[q + 1] != Text[i]:
            q = next_list[q]
        if Pattern[q + 1] == Text[i]:
            q = q + 1
        if q == m - 1:
            print_string(i - m + 1)
            q = next_list[q]
            count += 1

    print("Total %d number of pattern found!" % count)


def print_string(i):
    print('\nPattern found in : [ %d - %d ]:\n %s' % (i, i + m - 1, Text))
    print(' %s^%s^' % (' ' * i, ' ' * (m - 2)))
    print('\n')


kmp_algorithm()
