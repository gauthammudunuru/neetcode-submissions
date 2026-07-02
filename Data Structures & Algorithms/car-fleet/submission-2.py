class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:        
        Map={}
        
        for p,s in zip(position,speed):
            Map[target-p] = (target-p)/s       
        race_p = sorted(Map.keys())
        n = len(race_p)
        count = min(1,n)
        print(Map)
        val = Map[race_p[0]]
        for i in range(1,n):
            if Map[race_p[i]]>val:                
                count+=1          
                val=Map[race_p[i]]       
        return count 