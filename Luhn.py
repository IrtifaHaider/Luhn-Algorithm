def verify_card_number(card_number):
    card_number_reversed = card_number[::-1]#Step-02: Reverse card number

    sum_of_odd_digits = 0#Step-03: Extract and Sum Odd Position Digits
    odd_digits = card_number_reversed[::2]
    #print(odd_digits)
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)
    #print(sum_of_odd_digits)

    sum_of_even_digits = 0#Step-04: Extract, Process, and Sum Even Position Digits
    even_digits = card_number_reversed[1::2]
    #print(even_digits)
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
        #print(sum_of_odd_digits)
    total = sum_of_odd_digits + sum_of_even_digits#Step-05: Calculate the Total Sum
    #print(total)
    return total % 10 == 0#Step-06: Validation Check

def main():
    while True:
        card_number = input("Enter Your Card Number: ")
        card_translation = str.maketrans({'-': '', ' ': ''})#Step-01: Remove non-digit characters
        translated_card_number = card_number.translate(card_translation)
        if verify_card_number(translated_card_number):#Step-07: Call Verification Function
            print('The Card Number is Valid!')
            break
        else:
            print('The Card Number is INVALID!\nEnter Valid Card Number.')

main()