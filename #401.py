'''A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.

For example, the below binary watch reads "4:51".


Given an integer turnedOn which represents the number of LEDs that are currently on (ignoring the PM), return all possible times the watch could represent. You may return the answer in any order.

The hour must not contain a leading zero.

For example, "01:00" is not valid. It should be "1:00".
The minute must consist of two digits and may contain a leading zero.

For example, "10:2" is not valid. It should be "10:02".
 

Example 1:

Input: turnedOn = 1
Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
'''
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
      
        # Iterate through all possible hours (0-11)
        for hour in range(12):
            # Iterate through all possible minutes (0-59)
            for minute in range(60):
                # Count the number of 1s in binary representation of both hour and minute
                # bin() returns string like '0b101', so we count '1' characters
                hour_bits = bin(hour).count('1')
                minute_bits = bin(minute).count('1')
              
                # Check if total lit LEDs matches the required number
                if hour_bits + minute_bits == turnedOn:
                    # Format time as "H:MM" (hour without leading zero, minute with leading zero)
                    time_string = f"{hour}:{minute:02d}"
                    result.append(time_string)
      
        return result