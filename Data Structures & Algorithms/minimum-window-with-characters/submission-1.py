from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        st,end=0,0
        n=len(s)
        s_dict={}
        t_dict=Counter(t)
        t_len=len(t_dict.keys())
        res=""
        # out = []
        found=False
        while end<n and st<=end:
            if not found:
                s_dict[s[end]]=s_dict.get(s[end],0)+1
                # print(s_dict, s[st:end+1])
            count=0
            for k,v in t_dict.items():
                if s_dict.get(k,0)>=v:
                    count+=1
            if count==t_len:
                found=True
                # out.append(s[st:end+1])
                # print(1, st,end,s[st:end+1])
                if res!="" and len(s[st:end+1])<len(res):
                    res=s[st:end+1]
                elif res=="" and len(s[st:end+1])>0:
                    res=s[st:end+1]
                s_dict[s[st]]-=1
                st+=1
                # print(2, st,end,s[st:end+1])
            else:
                found=False
                end+=1
        # print(out)
        return res