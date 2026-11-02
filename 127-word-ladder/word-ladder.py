from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0 

        buckets = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[ : j] + "*" + word[j+1 :]
                buckets[pattern].append(word)

        visit = set([beginWord])
        q = deque([beginWord])
        res = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[ : j] + "*" + word[j+1 :]
                    for wordInBucket in buckets[pattern]:
                        if wordInBucket not in visit:
                            visit.add(wordInBucket)
                            q.append(wordInBucket)
            res += 1
        return 0

