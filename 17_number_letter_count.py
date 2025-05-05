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

        if x // 1000 > 0 and (x % 1000 > 0):
            letter_number += "and"
        elif x // 100 > 0 and (x % 100 > 0):
            letter_number += "and"
        
        if x // 1000 > 0:
            letter_number += self.thousands
            letter_number += self.numbers[x // 1000]

        if 0 < (x // 100) % 100 < 10:
            letter_number += self.hundreds
            letter_number += self.numbers[(x // 100) % 100]
        
        if (x // 10) % 10 > 0:
            if (x // 10) % 10  == 1:
                letter_number += self.teens[x % 100]
            else:
                letter_number += self.tens[(x // 10) % 10]

        if x % 10 > 0 and (x // 10) % 10 != 1:
            letter_number += self.numbers[x % 10]

        return letter_number


        
    
    

if __name__ == "__main__":

    solution = Solution()
    print(solution.NumberLetterCount(1,1000))

    # print((112 // 10) % 10)




