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