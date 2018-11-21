from collections import deque


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        
        def construct_dict(word_list):
            d = {}
            for word in word_list:
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i+1:]
                    d[s] = d.get(s, []) + [word]
            return d
            
        def bfs_words(begin, end, dict_words):
            queue, visited = deque([(begin, 1)]), set()
            while queue:
                word, steps = queue.popleft()
                if word not in visited:
                    visited.add(word)
                    if word == end:
                        return steps
                    for i in range(len(word)):
                        # s = word[:i] + "_" + word[i+1:]
                        print(s)
                        neigh_words = dict_words.get(s, [])
                        # print(neigh_words)
                        for neigh in neigh_words:
                            if neigh not in visited:
                                queue.append((neigh, steps + 1))
                        print(queue)
                    # break
            return 0
        
        d = construct_dict(set(wordList))
        # print(d)
        return bfs_words(beginWord, endWord, d)

#     class Solution:
#     def ladderLength(self, beginWord, endWord, wordList):
#         """
#         :type beginWord: str
#         :type endWord: str
#         :type wordList: List[str]
#         :rtype: int
#         """
#         if len(wordList) == 0:
#             return 0
#         if endWord not in wordList:
#             return 0
#         if not beginWord == wordList[0]:
#             wordList.insert(0, beginWord)
#         i = 0
#         lis = []
#         while i < len(wordList):
#             if self.compare(wordList[i], endWord):
#                 if wordList[i] not in lis:
#                     lis.append(wordList[i])
#                 lis.append(endWord)
#                 break
#             elif self.compare(wordList[i], wordList[i+1]):
#                 if wordList[i] not in lis:
#                     lis.append(wordList[i])
#                 lis.append(wordList[i+1])
#                 i += 1
#             else:
#                 break
#         return len(lis)

        
#     def compare(self, worda, wordb):
#         worda = list(worda)
#         wordb = list(wordb)
#         for i in worda:
#             if i in wordb:
#                 del wordb[wordb.index(i)]
#         if len(wordb) == 1 or len(wordb) == 0:
#             return True
#         else:
#             return False
