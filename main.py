def shorten_string(user_input):
    shortened_string = '' + user_input[0] + user_input[-1]
    return shortened_string

print(shorten_string('Packers'))

def peanut_butter_jelly_time():
    for pbj_number in range(101):
        if pbj_number % 3 == 0 and pbj_number % 5 == 0:
            print('Peanut Butter Jelly')
        elif pbj_number % 3 == 0:
            print('Peanut Butter')
        elif pbj_number % 5 == 0:
            print('Jelly')
        else:
            print(pbj_number)
peanut_butter_jelly_time()

def count_word(word):
    final_result = ''
    counter = 0
    while counter < len(word)-1:
        for index in range(0, len(word), 1):
            final_result += word[index]
            final_result += str(counter)
            counter += 1
    print(final_result)
input_string = input('Please input a word to match letters to string count. ')
count_word(input_string)

ingredients_list = ['peanut butter', 'jelly']

def search_list(user_input):
    input_search = user_input.lower()
    if input_search in ingredients_list:
        print(user_input + ' is on the list of ingredients.')
    elif input_search != ingredients_list:
        repeat = input('Sorry that ingredient was not found. Would you like to search again? Enter y/n: ')
        if repeat.lower() == 'y':
            search_list(input('Please enter your next ingredient to search. '))
        elif repeat.lower() == 'n':
            print('Goodbye.')
        else:
            print('Error - input not recognized.')
check_list = search_list(input('Please enter the ingedient to seach for. '))

input_list = ['Yellow', 'Purple', 'Orange']

def reverse_list(input):
    reversed_list = []
    for index in input:
        reversed_list = [index] + reversed_list
    return reversed_list
print(reverse_list(input_list))

names_list = ['Rebecca', 'Sam', 'Bob', 'Dante', 'Monica', 'Brad']

def verify_name_length(input_list):
    verified_names = []
    for index in input_list:
        if len(index) >= 5:
            verified_names += [index]
    return verified_names
print(verify_name_length(names_list))