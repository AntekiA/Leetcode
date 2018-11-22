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
        intervals = sorted(intervals, key=lambda i:i.start)
        nid = newid = intervals.index(newInterval)
        i = 1
        len_ = len(intervals)
        while i < len_ - newid:
            if intervals[newid].end >= intervals[newid+1].start:
                if intervals[newid].end >= intervals[newid+1].end:
                    del intervals[newid+1]
                    i += 1
                    continue
                else:
                    intervals[newid].end = intervals[newid+1].end
                    del intervals[newid+1]
                    i += 1
                    continue
            i += 1
        j = 0
        while j < nid:
            if intervals[newid-1].end >= intervals[newid].start:
                if intervals[newid-1].end >= intervals[newid].end:
                    del intervals[newid]
                    break
                else:
                    intervals[newid-1].end = intervals[newid].end
                    del intervals[newid]
                    newid -= 1
                    j += 1
                    continue
            j += 1
        return intervals
