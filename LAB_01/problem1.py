def Parity_Checker(Number):
    global even_count
    global odd_count
    global noparity_count
    if '.' in Number:
        noparity_count = noparity_count + 1
        return 'cannot have parity'
    elif (int(Number) & 1 == 0):
        even_count = even_count + 1
        return 'has even parity'
    else:
        odd_count = odd_count + 1
        return 'has odd parity'

def Palindrome_Checker(Word):
    global palindrome_count
    global nonpalindrome_count
    if Word == "":
        nonpalindrome_count = nonpalindrome_count + 1
        return 'not a palindrome'
    else:
        N = len(Word)
        for i in range (0, N//2, 1):
            if Word[i] != Word[N - 1 - i]:
                nonpalindrome_count = nonpalindrome_count + 1
                return 'not a palindrome'
        palindrome_count = palindrome_count + 1
        return 'a palindrome'

even_count = 0
odd_count = 0
noparity_count = 0
palindrome_count = 0
nonpalindrome_count = 0
j = 0
input_data = open('E:\\input.txt', 'r')
output_data = open('E:\\output.txt', 'w')
record_data = open('E:\\record.txt', 'w')
while True:
    r = input_data.readline().strip()
    s = r.split(' ')
    print (s)
    if len (s) == 1:
        break
    Number = s[0]
    Word = s[1]
    print(s[0], Parity_Checker(Number), 'and', s[1], 'is', Palindrome_Checker(Word), file=output_data)
    j = j+1
total = even_count + odd_count + noparity_count
print('Percentage of odd parity:', (odd_count / total) * 100, '%', file=record_data)
print('Percentage of even parity:', (even_count / total) * 100, '%', file=record_data)
print('Percentage of no parity:', (noparity_count / total) * 100, '%', file=record_data)
print('Percentage of palindrome:', (palindrome_count / total) * 100, '%', file=record_data)
print('Percentage of non-palindrome:', (nonpalindrome_count / total) * 100, '%', file=record_data)
input_data.close()
output_data.close()
record_data.close()

