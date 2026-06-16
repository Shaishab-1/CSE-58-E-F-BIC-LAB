from collections import defaultdict

def hamming_distance(s1, s2):
    count = 0

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1

    return count

def neighbors(pattern, d):

    if d == 0:
        return {pattern}

    if len(pattern) == 1:
        return {"A", "C", "G", "T"}

    result = set()

    suffix_neighbors = neighbors(pattern[1:], d)

    for text in suffix_neighbors:

        if hamming_distance(pattern[1:], text) < d:

            for nucleotide in "ACGT":
                result.add(nucleotide + text)

        else:
            result.add(pattern[0] + text)

    return result

def frequent_words_with_mismatches(text, k, d):

    frequency = defaultdict(int)

    for i in range(len(text) - k + 1):

        pattern = text[i:i + k]

        # Generate neighbors
        for neighbor in neighbors(pattern, d):
            frequency[neighbor] += 1

    max_count = max(frequency.values())

    result = []

    for pattern in frequency:
        if frequency[pattern] == max_count:
            result.append(pattern)

    return sorted(result)


text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4
d = 1

answer = frequent_words_with_mismatches(text, k, d)

print(" ".join(answer))
