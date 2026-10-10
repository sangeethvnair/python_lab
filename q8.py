def count(text):
    freq = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            freq[char] = freq.get(char, 0) + 1

    return freq
freq = {}
str1 = input("Enter a string : ")
freq = count(str1)
for ch2, count in freq.items():
    print(ch2," : ",count)