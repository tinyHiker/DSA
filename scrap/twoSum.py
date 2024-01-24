

def is_unique(s: str) -> bool:
    set_test = list(set(list(s)))
    test = list(s)
    
    if len(set_test) == len(test):
        return True
    
    return False
    

            
def lengthOfLongestSubstring( s: str) -> int:
    if len(s) == 1:
        return 1
    answer = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            sub_str = s[i:j+1]
            if is_unique(sub_str) and len(sub_str) > answer:
                answer = len(sub_str)
        
    return answer

print(lengthOfLongestSubstring("a"))

    