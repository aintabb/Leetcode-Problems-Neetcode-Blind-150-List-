"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.


Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""


# Time Complexity:  O(N)
# Space Complexity: O(N)
class ProductsOfArrayExceptSelf:
    def __init__(self) -> None:
        err_msg_invalid_products_array = (
            "The products array does not seem to be correct. Something is wrong!"
        )
        nums = [1, 2, 3, 4]

        result = self.product_except_self(nums)
        assert result == [24, 12, 8, 6], err_msg_invalid_products_array
        print(result)

        nums = [-1, 1, 0, -3, 3]

        result = self.product_except_self(nums)
        assert result == [0, 0, 9, 0, 0], err_msg_invalid_products_array
        print(result)

    def product_except_self(self, nums: list) -> list[int]:
        result = [1] * (len(nums))

        product = 1
        for i in range(len(nums)):
            result[i] = product
            product *= nums[i]

        product = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= product
            product *= nums[i]

        return result


productsOfArrayExceptSelf = ProductsOfArrayExceptSelf()
