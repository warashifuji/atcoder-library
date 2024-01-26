# 転倒数を求める
def count_inversions(arr):
    n = len(arr)
    inv_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inv_count += 1
    return inv_count

# 例の列
initial = [1, 2, 3, 4]
final = [1, 4, 3, 2]

# 必要な操作回数を求める
operations = count_inversions([initial.index(x) + 1 for x in final])
print(operations)
