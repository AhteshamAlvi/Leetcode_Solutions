class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []

        def dfs(index, expr, value, last):
            if index == len(num) and value == target:
                result.append(expr)

            for i in range(index, len(num)):
                curr = num[index:i+1]
                c_val = int(curr)
                
                if i > index and num[index] == '0':
                    break

                if index == 0:
                    dfs(i + 1, curr, c_val, c_val)
                else: 
                    dfs(i + 1, expr + '+' + curr, value + c_val, c_val)
                    dfs(i + 1, expr + '-' + curr, value - c_val, -c_val)
                    dfs(i + 1, expr + '*' + curr, value - last + (last * c_val), (last * c_val))

            pass
        
        dfs(0, "", 0, 0)
        return result