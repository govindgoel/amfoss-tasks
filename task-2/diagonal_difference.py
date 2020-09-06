def diagonal_difference(mat):
    return 0

mat= []
N =int(input())
for i in range(N):
    mat.append(map(int, raw_input().split()))

print (diagonal_difference(mat))
