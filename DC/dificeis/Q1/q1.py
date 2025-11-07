from typing import List
import sys

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        sys.setrecursionlimit(10**6)
        # Transformação: A[i] = nums1[i] - nums2[i].
        A = [a - b for a, b in zip(nums1, nums2)]
        
        # sort_count retorna (contagem_de_pares, array_ordenado)
        def sort_count(arr: List[int]):
            n = len(arr)
            if n <= 1:
                return 0, arr
            mid = n // 2
            left_count, left = sort_count(arr[:mid])
            right_count, right = sort_count(arr[mid:])
            cnt = left_count + right_count

            # contar pares cruzados: para cada x em left, contar quantos y em right
            # satisfazem: x <= y + diff  <=> y >= x - diff
            j = 0
            len_right = len(right)
            for x in left:
                # avançar j até encontrar primeiro right[j] >= x - diff
                while j < len_right and right[j] < x - diff:
                    j += 1
                cnt += (len_right - j)

            # mesclagem clássica (merge) para manter a ordenação ascendente
            merged = []
            i = 0
            j2 = 0
            while i < len(left) and j2 < len(right):
                if left[i] <= right[j2]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j2])
                    j2 += 1
            if i < len(left):
                merged.extend(left[i:])
            if j2 < len(right):
                merged.extend(right[j2:])

            return cnt, merged

        result, _ = sort_count(A)
        return result
