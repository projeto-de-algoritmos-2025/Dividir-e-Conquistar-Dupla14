class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Garantir que nums1 seja o menor array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2

        left, right = 0, m
        while left <= right:
            i = (left + right) // 2  # Partição em nums1
            j = half - i              # Partição em nums2

            # Valores de borda (usar ±inf para simplificar)
            left1 = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')
            left2 = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')

            # Verificar se a partição está correta
            if left1 <= right2 and left2 <= right1:
                # Caso o total seja par
                if total % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                # Caso o total seja ímpar
                else:
                    return min(right1, right2)
            elif left1 > right2:
                right = i - 1  # Mover para a esquerda
            else:
                left = i + 1   # Mover para a direita
