#Replace Words

class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        dictionary_set = set(dictionary)
        # max length of the roots available
        max_root_len = len(max(dictionary_set, key=len))
        sent = []
        for word in sentence.split(" "):
            for idx in range(len(word)):
                if idx <= max_root_len:
                    if word[:idx] in dictionary_set:
                        # find the best solution
                        word_set = set([word[:idx]])
                        word = min(word_set & dictionary_set)
                        break
                else:
                    break
            sent.append(word)
        return " ".join(sent)