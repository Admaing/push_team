# 滑动窗口

首先初始化窗口的左右边界，
右边界不断增加，每当进入一个新的字符时，计算当前字符所在的坑（freq[s[right]-‘a’],计算当前字符是否存在）是否被占，即是否有重复字符，如果存在重复字符，则滑动窗口左边右移，并将坑位的左面置为0，直到重复的字符移出了左边界，以此类推，最终最大的值为题目所解。

```go
func lengthOfLongestSubstring(s string) int {
    var freq [256]int
    if len(s)==0{
        return 0
    }
    
```

```go
left,right,result:=0, 0, 0
for left<len(s){
    if right<len(s)&&freq[s[right]-'a']==0{
        //判断当前坑是否被占
        freq[s[right]-'a']++
        right++
    }else{
        freq[s[left]-'a']--
        left++
    }
    result = max(result,right-left)
}
return result}
```
```go
func max(a int,b int) int{
    if a>b{
        return a
    }
    return b
}


```





# 最长回文子串

动态规划

特判：小于二的时候一定是回文串

状态方程：

```go
func longestPalindrome(s string) string {
	if len(s) < 2 {
		return s
	}
	println(len(s))

	maxlen := 1

	dp := make([][]bool, len(s))
	for i := 0; i < len(s); i++ {
		dp[i] = make([]bool, len(s))
	}


	begin := 0
	for L := 2; L <= len(s); L++ {
		for i := 0; i < len(s); i++ {
			j := L + i - 1
			if j >= len(s) {
				break
			}

			if s[i] != s[j] {
				dp[i][j] = false
			} else {
				if j-i < 3 {
					dp[i][j] = true
				} else {
					dp[i][j] = dp[i+1][j-1]
				}
			}

			if dp[i][j] == true && j-i+1 > maxlen {
				maxlen = j - i + 1
				begin = i
			}

		}

	}

	return s[begin : begin+maxlen]
}

```

## 星期二
