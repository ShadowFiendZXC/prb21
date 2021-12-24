print("Ведите символы")
s = input()
dictionary = dict()
for i in range(len(s)):
    if s[i] not in dictionary:
            dictionary[s[i]] = 1
    else:
            dictionary[s[i]] += 1

k = 0
for key in dictionary:
    if dictionary[key] == 1:
        k += 1

print(k)
