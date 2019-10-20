
# function which return reverse of a string 
def reverse(s): 
    return s[::-1] 
  
def isPalindrome(s): 
    # Checks if s is equal to reverse of s
    return s == reverse(s)
  
  
# Driver code 
s = "malayalam"
ans = isPalindrome(s) 
  
if ans: 
    print("Yes") 
else: 
    print("No") 
