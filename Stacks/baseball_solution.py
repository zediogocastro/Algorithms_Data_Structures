from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        curret_record = []
        pointer = 0
        for op in operations:
            if op == 'D':
                curret_record.append(2 * curret_record[pointer - 1])
                pointer += 1
            elif op == '+':
                curret_record.append(curret_record[pointer - 1] + curret_record[pointer - 2])
                pointer += 1
            elif op == 'C':
                curret_record.pop()
                pointer -= 1
            else:
                curret_record.append(int(op))
                pointer += 1
        return sum(curret_record)        