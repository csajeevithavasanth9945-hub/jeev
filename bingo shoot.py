class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        longest_prefix=""
        #shortest=min(len(strs[0]),len(strs[1]),len(strs[2]))
        for ind,i in range(len(strs)):
            if strs[ind][i]==strs[ind][i]==strs[ind][i]:
                longest_prefix+= strs[ind][i]
            else:
             #   print("no common element.")
             break
        return longest_prefix

strs=["flower","flollow","flow"]
obj=Solution()
print(obj.longestCommonPrefix(strs))