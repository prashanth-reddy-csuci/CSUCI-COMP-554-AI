
'''
HW1
'''

######### (100 points) ###########

'''
   1) write a function that gets a sentence (as a str) and outputs the length of the last word and the count of the characters in the sentence. 
   
   e.g.: input_sentence = 'Hello World!' --> output = [ 5 , 12 ]       
   e.g.: input_sentence = 'This is a sentence.' --> output = [ 8 , 19]
   

'''
# YOUR CODE GOES HERE




from math import sqrt
from collections import Counter
from string import ascii_uppercase as uc
from string import ascii_lowercase as lc



def LettersCounting(sentence):
    words = sentence.split()

    if len(words) == 0:
        return 'Empty sentence!!!'

    return [len([i for i in words[-1] if ord('A') <= ord(i) <= ord('Z') or ord('a') <= ord(i) <= ord('z')]), len(sentence)]


'''
    2)  write a function that gets two lists of numbers and merges them and outputs the sorted merged list.
   
   e.g.: input_list1 = [0,1,2,8,-1, 9] , input_list2 = [-11,9]--> output = [-11, -1, 0, 1, 2, 8, 9, 9]
   
'''
# YOUR CODE GOES HERE


def ListSorting(list_a, list_b):
    return sorted(list_a + list_b)


'''
    3)  write a function that get a list of numbers and outputs the second largest number in it.
   
   e.g.: input_list = [0,1,2,8,-1] --> output = 2
   e.g.: input_list = [-11, 1.2, 9.9,9] --> output = 9
'''
# YOUR CODE GOES HERE


def SecondMaximum(input_list):
    if len(input_list) < 2:
        return 'List must contain atleast 2 numbers.'

    first_max = float('-inf')
    second_max = float('-inf')

    for number in input_list:
        if number >= second_max:
            if first_max < number:
                second_max = first_max
                first_max = number
            else:
                second_max = number

    return second_max


'''
    4)  write a function that get a string as an input and outputs the reverse of that (only letters!)
   
   e.g.: input_str = 'hel-lo,wo.rld' --> output = 'dlr-ow,ol.leh'
   e.g.: input_str = '12311!hm' --> output = '12311!mh'
'''
# YOUR CODE GOES HERE


def LettersReverse(input_str):
    input_str = list(map(str, input_str))
    input_str_length = len(input_str)
    current_pos = input_str_length - 1
    pointer = 0

    while pointer < current_pos:
        if input_str[pointer] not in lc and input_str[pointer] not in uc:
            pointer += 1
            continue

        if input_str[current_pos] not in lc and input_str[current_pos] not in uc:
            current_pos -= 1
            continue

        input_str[pointer], input_str[current_pos] = input_str[current_pos], input_str[pointer]
        pointer += 1
        current_pos -= 1

    return "".join(input_str)


'''
    5)  write a function that gets a sentence (as a str) and outputs the reverse of that.
   
   e.g.: input_sentence = 'Hello World' --> output = 'World Hello'
   e.g.: input_sentence = 'this is a sentence' --> output = 'sentence a is this'
'''
# YOUR CODE GOES HERE


def SentenceReverse(input_sentence):
    input_sentence = input_sentence.split()
    input_sentence.reverse()
    return ' '.join(input_sentence)


'''
    6)  write a function that gets two numbers as strings and outputs the sum of them. 
   
   e.g.: str1 = '96' , sr2 = '21'--> output = 117
   e.g.: str1 = '28' , sr2 = '2'--> output = 30
'''
# YOUR CODE GOES HERE


def StringSum(str1, str2):
    try:
        int_str1, int_str2 = int(str1), int(str2)
        return int_str1 + int_str2
    except Exception as e:
        return e


'''
    7)  write a function that gets two binary numbers from the user and outputs the sum of them in binary. 
   
   e.g.: input1 = 101 , input2 = 10 --> output = 111
   e.g.: input1 = 11 , input2 = 1 --> output = 100
'''
# YOUR CODE GOES HERE


def BinarySum(str1, str2):
    try:
        result = int(str1, 2) + int(str2, 2)
        return bin(result)[2:]
    except Exception as e:
        return e


'''
    8)  write a function:
    
        5-1) thats gets a list of numbers and counts the occurrences of all items in it. 
              e.g.: list1 = [9,9,1,0,1,9] --> output = [(9,3) , (1,2), (0,1)]
              
        5-2) that gets two lists and outputs their common elements. 
             e.g.: list1 = [66,23,1,0,1,9] , list2 = [5,55,1,12] --> output = [1]         

'''
# YOUR CODE GOES HERE


def ElementsFrequency(list1):
    return list(Counter(list1).items())


def CommonElements(list1, list2):
    set1, set2 = set(list1), set(list2)
    return list(set1.intersection(set2))



'''
    9)  write a function that gets a string from the user and returns the most frequent character in it. 
   
   e.g.: str1 = 'hello world'--> output = 'l'
   e.g.: str1 = 'cs_comp478'--> output = 'c'
'''
# YOUR CODE GOES HERE


def FrequentElements(input_str):
    if not len(input_str):
        return 'Invalid Input. Input cannot be empty!'

    counter = Counter(input_str)
    max_repititive_characters = []
    max_repititive = max(counter.values())
    for k, v in counter.items():
        if v == max_repititive:
            max_repititive_characters.append(k)

    return max_repititive_characters


'''
    10) write a function that gets a list of numbers and returns the compnents of the list that are perfect square numbers. 
   
   e.g.: input1 = [1, 5, 8, 9] --> output = [1,9]
   e.g.: input1 = [3, 7, 5, 55 ]--> output = []

'''

# YOUR CODE GOES HERE


def PerfectSquareNumbers(list1):
    return [i for i in list1 if int(sqrt(i))**2 == i]


def main():

    # Problem 1
    print(LettersCounting('Hello World!'))
    print(LettersCounting('This is a sentence.'))
    # print(LettersCounting('sdfsdf'))
    # print(LettersCounting('sdfsdf!!!!!'))

    # Problem 2
    print(ListSorting([0, 1, 2, 8, -1, 9], [-11, 9]))
    # print(ListSorting([5, 2], [4, 1]))
    # print(ListSorting([], [-11, 9]))
    # print(ListSorting([0, 1, 2, 8, -1, 9], []))
    # print(ListSorting([], []))

    # Problem 3
    print(SecondMaximum([0, 1, 2, 8, -1]))
    print(SecondMaximum([-11, 1.2, 9.9, 9]))
    # print(SecondMaximum([3, 2, 1]))

    # Problem 4
    print(LettersReverse("hel-lo,wo.rld"))
    print(LettersReverse("12311!hm"))

    # Problem 5
    print(SentenceReverse('Hello World'))
    print(SentenceReverse('this is a sentence'))

    # Problem 6
    print(StringSum('96', '21'))
    print(StringSum('28', '2'))

    # Problem 7
    str1 = input('Enter a number in binary format A: ')
    str2 = input('Enter a number in binary format B: ')

    print(BinarySum(str1, str2))

    # Problem 8
    print(ElementsFrequency([9, 9, 1, 0, 1, 9]))
    # print(ElementsFrequency([]))

    print(CommonElements([66, 23, 1, 0, 1, 9], [5, 55, 1, 12]))

    # Problem 9
    input_str = input('Enter string: ')
    print(FrequentElements(input_str))

    # Problem 10
    print(PerfectSquareNumbers([1, 5, 8, 9]))
    print(PerfectSquareNumbers([3, 7, 5, 55]))


if __name__ == "__main__":
    main()
