# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals.append(newInterval)
        out = []
        for i in sorted(intervals, key=lambda i:i.start):
            if out and out[-1].end >= i.start:
                out[-1].end = max(out[-1].end, i.end)
            else:
                out += [i]
        return out
