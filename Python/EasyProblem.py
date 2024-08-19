'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order. '''
# use Dictionary for n and double for loop for n2

def two_sum(arr,targ):
    Dictionary = {}
    for n,x in enumerate(arr,1):
        try:
            return Dictionary[x], n
        except KeyError:
            Dictionary.setdefault(targ - x,n) # adding the required integer in dictionary

a = (1,2,3,2,7,1,15)
t = 9
print(two_sum(a,t))  # (1,2)
a = (-3,4,3,90)
t = 0
print(two_sum(a,t))  # (1,3)



# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def addTwoNumbers(l1, l2):
        lstr = ""
        lstr1 = ""
        dummy = ListNode()
        temp = dummy        
        while l1 is not None:
          lstr += str(l1.val)
          l1 = l1.next
        while l2 is not None:
          lstr1 += str(l2.val)
          l2 = l2.next
        lfinalstr = str(int(lstr[::-1])+int(lstr1[::-1]))
        print(lfinalstr)
        for sstr in lfinalstr:
          l = ListNode(int(sstr))
          temp.next = l
          temp = temp.next
        print("final")        
        return dummy.next

    
        #for val in reversed(l1):
         #  head = ListNode(val, head)


l = ListNode()
lt = ListNode()
lt3 = ListNode()
l.val =1
l.next=lt
lt.val =2
lt.next = lt3
lt3.val =3

l1 = ListNode()
ll1 = ListNode()
ll2 = ListNode()
l1.val =3
l1.next=ll1
ll1.val =2
ll1.next=ll2
ll2.val =2


print(l.val)

print(l1.val)
temp =addTwoNumbers(l,l1)
while temp is not None:
          print(temp.val)
          temp = temp.next


def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        nlen = len(s)
        nstrOutpu=1
        for value,sval in enumerate(s):
            print(sval,value)
            ntempstr = sval
            for i in range((value+1),nlen):
              if sval!=s[i] and 0==ntempstr.count(s[i]):
                ntempstr = ntempstr+s[i]
              else:
                break
            if nstrOutpu<len(ntempstr):
                nstrOutpu=len(ntempstr)

        return nstrOutpu

lengthOfLongestSubstring("abcabc")


def findMedianSortedArrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        narlen1 = len(nums1)
        narlen2 = len(nums2)
        i ,j = 0,0
        sortedArray = []
        while i<narlen1 and j<narlen2:
          if nums1[i] < nums2[j] :
                sortedArray.append(nums1[i])
                i+=1
          else:
                sortedArray.append(nums2[j])
                j+=1
        sortedArray = sortedArray + nums1[i:] + nums2[j:]

        print(sortedArray)
        nlen = len(sortedArray)%2
        nlenhalf = int(len(sortedArray)/2)
        if(0!=nlen):
           return (sortedArray[nlenhalf])
        else:
           return ((sortedArray[nlenhalf] + sortedArray[nlenhalf-1])/2)

n = findMedianSortedArrays([1,2], [3,4])
print(n)


def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        ostrlpalin = ""
        for j in range(0,len(s)):
            for i in range(len(s),j-1,-1):
                lpalin=  s[j:i]
                if lpalin==lpalin[::-1]:
                  if len(ostrlpalin)<=len(lpalin):
                        ostrlpalin = lpalin
                  break
                    
        
        print(ostrlpalin)
        return ostrlpalin

longestPalindrome("aabbaavvv")
longestPalindrome("bb")


#Daily challenge Given the root of a binary tree, each node in the tree has a distinct value.
#After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).
#Return the roots of the trees in the remaining forest. You may return the result in any order.

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
    
class Solution:
    #def delNodes(self, root: [TreeNode], to_delete: list[int]) -> List[TreeNode]:
      # depth first search , iterate over all nodes
        def disintegratedNodes(root):
            if root is None:
                return None
            
            root.left = disintegratedNodes(root.left)
            root.right = disintegratedNodes(root.right)
            if root.val not in s:
                return root
            if root.left:
                ans.append(root.left)
            if root.right:
                ans.append(root.right)
            return None

        #s = set(to_delete) #A set is a collection which is unordered, unchangeable*, and unindexed.
        # set contains only unique values
       # print(s)

        ans = []
        #if disintegratedNodes(root):
            #ans.append(root)
            #return ans

tr = TreeNode(1,2,3)
#delNodes(tr,[1,2])

# Graph Search Problem
# Adjancy matrix (too much space and difficult ot insert take quadratic time for 2d array) adjacency list(each element its own row)

# DFS depth first search
'''fun visit(N):
    if N is not Visited:
      visit(N)'''
#BFS breadth first search (iterate direct children and than grand children)

#cnt1 = Counter() use to count object in array [1,1,2,3,2] -> counter {"1":2, "2":2, "3":1}


def countPairs(self, root: TreeNode, distance: int) -> int:
        # depth first search algo
        def minimumDistance(root,distanceCnt,totalDistance):
            if root is None or totalDistance >= distance:
                return
            if root.left is None and root.right is None:
                distanceCnt[totalDistance] += 1
                return
            minimumDistance(root.left,distanceCnt,totalDistance+1)
            minimumDistance(root.right,distanceCnt,totalDistance+1)

        if root is None:
           return 0
        ans = self.countPairs(root.left, distance) + self.countPairs(
            root.right, distance
        ) 
        
        print(root,distance,1)

        distanceCnt1 = Counter()
        distanceCnt2 = Counter()
        minimumDistance(root.left, distanceCnt1, 1)
        minimumDistance(root.right, distanceCnt2, 1)
        print(distanceCnt1)
        print(distanceCnt2)
        for k1, v1 in distanceCnt1.items():
            for k2, v2 in distanceCnt2.items():
                if k1 + k2 <= distance:
                    ans += v1 * v2

        return ans


def palindrome(inputString):
    if len(inputString)==1 or len(inputString)==0:
        return len(inputString)
    
    freq = {}
    for c in inputString:
        freq[c] = freq.get(c, 0) + 1
    
    freqList = {}
    for key,val in enumerate(inputString):
      for j in range(key+1, len(inputString)): 
        if inputString[j]==val:
          freqList.setdefault(val, []).append(inputString[j])
    
    print(freqList)
    print(freq)
    lenPalin = 0
    bindividualVal=False
    for value in freq:
        if freq[value]%2==0:
            lenPalin+=freq[value]
        elif bindividualVal==False:
            lenPalin+=freq[value]
            bindividualVal=True
        else:
            lenPalin+=freq[value]-1
        
        
    print(lenPalin,freq)
    return lenPalin
    #freq = {a: 1, b: 1, c: 4, d: 2}

print(palindrome("aaaabbbdcccc"))