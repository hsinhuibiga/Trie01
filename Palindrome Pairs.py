#Palindrome Pairs

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        wmap = {w: i for i, w in enumerate(words)}

        def isPalindrome(word):
            _len = len(word)
            for x in range(_len / 2):
                if word[x] != word[_len - x - 1]:
                    return False
            return True

        res = set()
        for idx, word in enumerate(words):
            if word and isPalindrome(word) and "" in wmap:
                nidx = wmap[""]
                res.add((idx, nidx))
                res.add((nidx, idx))

            rword = word[::-1]
            if word and rword in wmap:
                nidx = wmap[rword]
                if idx != nidx:
                    res.add((idx, nidx))
                    res.add((nidx, idx))

            for x in range(1, len(word)):
                left, right = word[:x], word[x:]
                rleft, rright = left[::-1], right[::-1]
                if isPalindrome(left) and rright in wmap:
                    res.add((wmap[rright], idx))
                if isPalindrome(right) and rleft in wmap:
                    res.add((idx, wmap[rleft]))
        return list(res)