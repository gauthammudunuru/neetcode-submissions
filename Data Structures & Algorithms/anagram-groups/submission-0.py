class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for word in strs:
            k_list = [0]*26
            for ch in word:
                ind = ord(ch)-ord("a")
                k_list[ind]+=1
            key = tuple(k_list)
            if key in res:
                res[key].append(word)
            else:
                res[key] = [word]

        return list( res.values())