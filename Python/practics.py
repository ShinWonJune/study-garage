n = int(input())
decks = [int(input()) for _ in range(n)]
decks.sort()

counts = 0
i = 0
while i < n-2 :
    counts = decks[i] + decks[i+1]
    decks.append(counts)
    i += 1
sum(decks)