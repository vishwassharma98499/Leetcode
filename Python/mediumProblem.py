from collections import Counter
import collections
from typing import List

from collections import deque
import heapq

def partitionString( s: str) -> int:
        ans, mask = 1, 0
     
        for x in map(lambda c: ord(c) - ord("a"), s):
            print(mask >> x,x)
            if mask >> x & 1:
                ans += 1
                mask = 0

            print(mask,1 << x)
            mask |= 1 << x
            print(mask)
            #print(mask)

        
        print(ans)
        return ans

def partitionStringset( s: str) -> int:
        result = 1
        sett = set()
        for i in s:
            if i not in sett:
                sett.add(i)
            else:
                result += 1
                sett.clear()
                sett.add(i)

        return result

def kthFactor( n: int, k: int) -> int:
        flist = []
        
        if k>n: 
            return -1
        if n<=2:
            flist.append(1)

        for i in range(1,int(n/2)+1):
            if n%i==0 :
                flist.append(i)
        
        
           
        flist.append(n)
    
        flist.sort()
        #print(len(flist))
        #print(flist)
        llen = len(flist)-1
        if k-1<=llen:
            return flist[k-1]
        else:
             return -1 
        
        print(flist)


 
def optimize_box_weights(arr):
    # Sort the array in descending order
    arr.sort(reverse=True)
    
    total_sum = sum(arr)
    subset_a_sum = 0
    subset_a = []
    
    for i, weight in enumerate(arr):
        subset_a_sum += weight
        subset_a.append(weight)
        
        # Check if the current subset A satisfies the condition
        if subset_a_sum > total_sum - subset_a_sum:
            break
    
    # If all elements are needed, return the whole array sorted in ascending order
    if len(subset_a) == len(arr):
        return sorted(arr)
    
    # If no valid subset exists, return an empty array
    if subset_a_sum <= total_sum - subset_a_sum:
        return []
    
    # Return subset A in ascending order
    return sorted(subset_a)

# Test the function
test_cases = [
    [3, 7, 5, 6, 2],
    [4, 3, 2, 1],
    [1, 2, 3, 4, 5],
    [10, 10, 10, 10],
]

for case in test_cases:
    #result = optimize_box_weights(case)
    #print(f"Input: {case}")
    #print(f"Output: {result}")
    #print(f"Sum of A: {sum(result)}, Sum of B: {sum(case) - sum(result)}")
    print()


def canConstruct( ransomNote, magazine):
        st1, st2 = Counter(ransomNote), Counter(magazine)
        if st1 & st2 == st1:
            return True
        return False


def isValidSudoku( board):
        boardMap = collections.defaultdict(list)
        for x in range(9):
            for y in range(9):
                char = board[x][y]
                if char != '.': 
                    if char in boardMap:
                        for pos in boardMap[char]:
                            if (pos[0]== x) or (pos[1] == y) or (pos[0]//3 == x//3 and pos[1]//3 == y//3):
                                return False
                    boardMap[char].append((x,y))


def threeSum( nums: List[int]) -> List[List[int]]:
        print(nums)
        outArr = []
        nums.sort()
        #nums = list(set(nums))
        nlen = int(len(nums))
        for i in range(0,nlen-2):
            if i > 0 and nums[i] == nums[i - 1]:
               continue
            ni = nums[i]
            left, right = i + 1, nlen - 1

            while left < right:
               total = nums[i] + nums[left] + nums[right]
               if total == 0:
                 outArr.append([nums[i], nums[left], nums[right]])
                 left += 1
                 right -= 1
               elif total < 0:
                 left += 1
               else:
                 right -= 1
            
        res = list({*map(tuple, map(sorted, outArr))})
        return res


from collections import defaultdict

def count_subarrays_with_average(arr, k):
    n = len(arr)
    prefix_sum = 0
    count = 0
    sum_frequency = defaultdict(int)
    
    for i in range(n):
        # Subtract k from each element and calculate prefix sum
        prefix_sum += arr[i] - k
        
        # If prefix sum is 0, we've found a subarray with average k
        if prefix_sum == 0:
            count += 1
        
        # Add frequency of this prefix sum (if it exists)
        count += sum_frequency[prefix_sum]
        
        # Increment frequency of this prefix sum
        sum_frequency[prefix_sum] += 1
    
    return count

# Example usage
arr = [1, 2, 3, 4, 5]
k = 3
#result = count_subarrays_with_average(arr, k)
#print(f"Number of subarrays with average {k}: {result}")


#nums = [-9,14,-7,-8,9,1,-10,-8,13,12,6,9,3,-3,-15,-15,1,8,-7,-4,-6,8,2,-10,8,11,-15,3,0,-11,-1,-1,10,0,6,5,-14,3,12,-15,-7,-5,9,11,-1,1,3,-15,-5,11,-12,-4,-4,-2,-6,-10,-6,-6,0,2,-9,14,-14,-14,-9,-1,-2,-7,-12,-13,-15,-4,-3,1,14,3,-12,3,3,-10,-9,-1,-7,3,12,-6,0,13,4,-15,0,2,6,1,3,13,8,-13,13,11,11,13,14,-6]

#threeSum(nums)

#board = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
#isValidSudoku( board)
#canConstruct("aadd", "aacddd")
#kthFactor( 2,2)
#kthFactor( 46,4)
#partitionStringset("bbdddd")

clist = [1,2,3]
clist.pop()
clist.append(2)

# list as stack directly used as list.property
clist.pop()

# list as queue  use from collections import deque as insert is costly

queue = deque(["a","b","c"])
queue.append("d")
queue.appendleft("e")
queue.insert(4,"f")
queue.popleft()

# list comprehensions

squares = []
for x in range(10):
    squares.append(x**2)

# or the other way is 

squaresm = list(map(lambda x: 1,range(2)))


squaresm.append(1)
squaresm.append(1)


squaresmap = list(map(lambda x: x**2, range(10)))
squaresmap = [x**2 for x in range(10)]


# nested list or fro loop two in one line

combs = [[x,y] for x in [1,2,3] for y in [4,5,6,7] if x!=y  ]
combstuple = [(x,y) for x in [1,2,3] for y in [4,5,6,7] if x!=y  ]

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

lmatrix = [[row[i] for row in matrix] for i in range(len(matrix)+1)] 

item = zip([1, 2, 3], ['sugar', 'spice', 'everything nice'])

## Tuples are immutable:
# but they can contain mutable objects like array

#  A set is an unordered collection with no duplicate elements. 
listl = [1,1,2,3,4]
sset = set(listl)

ssetcomprehension = {1,1,2,3} #  {1,2,3} 
ssetcomprehension = {x for x in 'abrrrrracadabra' if x not in 'abc'}

# Dictionaries key value pair or hashmap

hmap = {'jack': 4098, 'sape': 4139}
hmap['guido'] = 4127
hmap['guido'] = 4128
print(list(hmap),hmap["jack"],sorted(hmap))
hmap = {item }

hmapCompre = {"v"+ str(x) :x**3 for x in range(6,3,-1)}
for k, v in hmapCompre.items():
    print(k, v)
#{2: 4, 4: 16, 6: 36}

j = [i for i in range(5)]
print(j)

# heap is sorted in form heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2]
def heapSort(arr):
    heapq.heapify(arr)
    return arr

arr = [9, 4, 3, 8, 10, 2, 5] 
print(heapSort(arr))
heapq.heappush(arr, 1)
heapq.heappush(arr, 6)
heapq.heappush(arr, 2)
print(arr)

print(heapq.heappop(arr))



