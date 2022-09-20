import sys
input = sys.stdin.readline
n = int(input())
sc = []
for i in range(n):
    sc.append(list(map(int,input().split())))
    
#끝나는 시간 기준으로 먼저 정렬,, 그러면 0 8 같은 상황을 피할 수 있다.        
sc.sort(key =lambda x:(x[1],x[0]))
count = 0
pre_end = 0

for start, end in sc:
    if pre_end <= start:
        count += 1
        pre_end = end
print(count)