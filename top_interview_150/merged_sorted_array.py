# # def merge(nums1, m, nums2, n) -> None:
# #     """
# #     Do not return anything, modify nums1 in-place instead.
# #     """
# #     p1 = m - 1
# #     p2 = len(nums1) - 1
# #     p3 = n - 1

#     # while p3 >= 0:
#     #     if nums2[p3] > nums1[p1]:
#     #         nums1[p2] = nums2[p3]
#     #         p2 = p2 - 1
#     #         p3 = p3 - 1
#     #     elif nums2[p3] <= nums1[p1]:
#     #         nums1[p2] = nums1[p1]
#     #         nums1[p1] = nums2[p3]
#     #         p1 = p1 - 1
#     #         p3 = p3 - 1 
#     #     else:
#     #         p1 = m - 1
#     #         p2 = len(nums1) - 1
#     #         p3 = n - 1            
      
#     # while p3 <= m + n - 1:
#     #     if nums2[p3] < nums1[p1]:
#     #         nums1[p2] = nums1[p2]

# def merge(nums1, m, nums2, n):
#         # """
#         # :type nums1: List[int]
#         # :type m: int
#         # :type nums2: List[int]
#         # :type n: int
#         # :rtype: None Do not return anything, modify nums1 in-place instead.
#         # """
#         # if n == 0 :return
#         # len1 = len(nums1)
#         # end_idx = len1-1
#         # while n > 0 and m > 0 :
#         #     print("this is n before if ", n)
#         #     if nums2[n-1] >= nums1[m-1]:
#         #         nums1[end_idx] = nums2[n-1]
#         #         n-=1
#         #         print("this is n after if ", n)
#         #     else:
#         #         nums1[end_idx] = nums1[m-1]
#         #         m-=1
#         #         print("test run ", m)
#         #     end_idx-=1
            
#         # while n > 0:
#         #     nums1[end_idx] = nums2[n-1]
#         #     print("this is n before -= ", n)
#         #     n-=1
#         #     end_idx-=1
#         #     print("this is n ", n)
#         #     print("this is end_idx ", end_idx)

 
# nums1 = [4,5,6,0,0,0]
# nums2 = [1,2,3]
# m = 3
# n = 3

# # nums1 = [1,2,3,0,5,6]
# # nums2 = [2,5,6]
# # m = 3
# # n = 3

# merge(nums1, m, nums2, n)
# print(nums1)

#     # if nums1[p1] > nums2[p3]:
#     #     asdf 
#     # elif nums1[p1] < nums2[p3]:
#     #     asdf



# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         p1 = m - 1
#         p2 = len(nums1) - 1
#         p3 = n - 1

#         while p3 >= 0:
#             if nums2[p3] > nums1[p1]:
#                 nums1[p2] = nums2[p3]
#                 p2 = p2 - 1
#                 p3 = p3 - 1
#             elif nums2[p3] <= nums1[p1]:
#                 nums1[p2] = nums1[p1]
#                 nums1[p1] = nums2[p3]
#                 p1 = p1 - 1
#                 p3 = p3 - 1   
#             else
#                 p1 = m - 1
#                 p2 = len(nums1) - 1
#                 p3 = n - 1                   

#         while p3 <= m + n - 1:
#             if nums2[p3] < nums1[p1]:
#                 nums1[p2] = nums1[p2]