class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(left, right)

    def merge(self, left: list[int], right: list[int]) -> list[int]:
        merged = []
        i = j = 0

        # Combinar elementos em ordem
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        # Adicionar os elementos restantes
        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged
