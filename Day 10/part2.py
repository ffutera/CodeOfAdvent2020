import copy
import math
f = open("d10.txt","r")
data = [int(d) for d in f.read().split("\n")]
data.append(max(data)+3) #to account for devices power foltage
data.sort() #Sorted  array utilizing each adapter
#not my code :(
def part_two(parsed_input):
    # Add charging outlet and device to list of adapters
    parsed_input += [0, max(parsed_input)+3]
    parsed_input = sorted(parsed_input)

    dp = [0]*len(parsed_input)
    # There's only one path to the charging outlet
    dp[0] = 1
    for i in range(1, len(parsed_input)):
        sm = 0
        for j in range(1,4): # 1, 2, 3
            if i-j < 0:
                # Skip out-of-range checks at the start of the process
                continue
            if parsed_input[i]-parsed_input[i-j] <= 3:
                # Candidate adapter
                sm += dp[i-j]
        dp[i] = sm
    return dp[-1]

print(part_two(data))