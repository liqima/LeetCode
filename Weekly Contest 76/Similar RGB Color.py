class Solution:
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        number = '0123456789abcdef'
        res = 0
        reg = ''
        for i in range(1, len(color), 2):
            print(color[i:i + 2])
            current = color[i:i + 2]
            hex_value = number.index(current[0]) * 16 + number.index(current[1])
            print(hex_value)

            start = '0'
            final_diff = hex_value ** 2
            for k in range(1, len(number)):
                double_color = number[k] + number[k]
                hex_color = number.index(double_color[0]) * 16 + \
                    number.index(double_color[1])
                current_diff = (hex_value - hex_color) ** 2
                if current_diff < final_diff:
                    final_diff = current_diff
                    start = number[k]
            res += final_diff
            reg += start + start
        reg = '#' + reg
        return reg



s = Solution()
print(s.similarRGB("#1c9e03"))