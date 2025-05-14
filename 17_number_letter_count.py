"""
If the numbers to are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.


If all the numbers from 1 to (one thousand) inclusive were written out in words, how many letters would be used? 

NOTE: Do not count spaces or hyphens. For example,
(three hundred and forty-two) contains 23 letters and (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

"""
# O(n) time complexity where n is the list of numbers to iterate through with O(1) space complexity discounting the different dictionaries in class
class Solution:

    # Dictionaries storing all items needed to convert words to the letter form of themselves
    thousands = "thousand"
    hundreds = "hundred"
    tens = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
    teens = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
    numbers = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}

    def NumberLetterCount(self, low_num: int, high_num: int) -> int:

        total_count = 0

        # Iterate through each number and convert it before measuring it
        for x in range(low_num, high_num + 1):
            letter_number = self.numberfier(x)
            total_count += len(letter_number)
            # print(letter_number, len(letter_number), total_count)

        return total_count
            

    # Starting from checking whether 'and' is necessary, start from the 1000s place and go down
    def numberfier(self, x: int) -> str:

        letter_number = ""

        # If the number is in the thousands and there are numbers > 0 in the 
        # hundreds, tens, or ones place...add 'and'
        if x // 1000 > 0 and (x % 1000 > 0):
            letter_number += "and"
        # Else if the number is in the hundreds and there are numbers in the tens or ones > 0
        # ...add 'and'
        elif x // 100 > 0 and (x % 100 > 0):
            letter_number += "and"
        
        # if number is in thousands, add 'thousand' and then determine in what thousands place it is in 1,2,3,4...
        if x // 1000 > 0:
            letter_number += self.thousands
            # pull just the digit in the thousands place
            letter_number += self.numbers[x // 1000]

        # If there is a number in the hundreds place and it is less than 10 (special case handled by next...)
        if 0 < (x // 100) % 100 < 10:
            letter_number += self.hundreds
            letter_number += self.numbers[(x // 100) % 100]
        
        # If there is a number in the tens place...
        if (x // 10) % 10 > 0:
            # if it is 1 then it must be between 10 and 19....
            if (x // 10) % 10  == 1:
                letter_number += self.teens[x % 100]
            # Else it is is 20-90
            else:
                letter_number += self.tens[(x // 10) % 10]

        # Check what the 1s digit is and andd it 
        if x % 10 > 0 and (x // 10) % 10 != 1:
            letter_number += self.numbers[x % 10]

        return letter_number


        
    
    

if __name__ == "__main__":

    solution = Solution()
    print(solution.NumberLetterCount(1,1000))

    # print((112 // 10) % 10)




