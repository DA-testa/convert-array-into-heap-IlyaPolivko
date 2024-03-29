# python3
import re


def build_heap(data):
    n = len(data)
    swaps = []
    for i in range(n // 2, -1, -1):
        swaps = sift_down(data, i, swaps)
    return swaps

def sift_down(data, i, swaps):
    n=len(data)
    min_index = i
    l = 2 * i +1
    if l < n and data[l] < data[min_index]:
        min_index =1
    r = 2 * i + 2
    if r < n and data[r] < data[min_index]:
        min_index = r
    if i != min_index:
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        swaps = sift_down(data, min_index, swaps)
    return swaps
    
def main():
    input_string = input()
    match = re.match(r'^\d+$', input_string.strip())
    if match is None:
        raise ValueError('Invalid input: {}'.format(input_string.strip()))
    n = int(match.group(0))
    data = list(map(int, input().split()))
    assert len(data) == n
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
