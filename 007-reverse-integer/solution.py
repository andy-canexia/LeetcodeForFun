class Solution:
    def reverse(self, x: int) -> int:

        is_negative = x < 0

        if is_negative:
            p_int = -1 * x
        else:
            p_int = x

        result = 0
        while p_int > 0:
            result *= 10
            result += p_int % 10
            p_int = int(p_int/10)

        # overflow issue
        if result > pow(2, 31):
            return 0

        if is_negative:
            return -1 * result
        return result
