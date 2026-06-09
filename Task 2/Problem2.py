text = input().strip()
pattern = input().strip()

count = 0

k = len(pattern)

for i in range(len(text) - k + 1):
  if text[i:i+k] == pattern:
    count += 1

print(count) 
