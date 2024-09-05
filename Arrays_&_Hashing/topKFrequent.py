class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_w_counts = {}
        for element in nums:
            if element in dict_w_counts:
                dict_w_counts[element] += 1
            else:
                dict_w_counts[element] = 1
        x = dict(
            sorted(dict_w_counts.items(), key=lambda x: x[1], reverse=True)
        )
        return list(x.keys())[:k]