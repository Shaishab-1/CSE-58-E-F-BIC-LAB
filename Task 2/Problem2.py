text = input().strip()
k = int(input())

counts = {}

for i in range(len(text) - k + 1):
  pattern = text[i:i+k]

  if pattern in counts:
    counts[pattern] += 1
  else:
    counts[pattern] = 1

  max_count = max(counts.values())

  result = []

  for pattern in counts:
    if counts[pattern] == max_count:
      result.append(pattern)

print(result)
