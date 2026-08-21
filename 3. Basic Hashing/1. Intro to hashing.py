#hashing - prestoring and fetching


arr = [1, 2, 2, 3, 1, 2, 4]

freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)

