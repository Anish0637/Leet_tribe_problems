from functools import reduce
from collections import defaultdict
class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
#        words="hack"
        Trie = lambda : defaultdict(Trie)
        trie = Trie()
        for w in words:
            end = reduce(dict.__getitem__, w, trie)
            end['#'] = '#'
            end['$'] = w

        self.res = set()
        self.used = [[False] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.find(board, i, j, trie)
        return list(self.res)

    def find(self, board, i, j, trie):
        if '#' in trie:
            self.res.add(trie['$'])
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        if not self.used[i][j] and board[i][j] in trie:
            self.used[i][j] = True
            self.find(board, i + 1, j, trie[board[i][j]])
            self.find(board, i, j + 1, trie[board[i][j]])
            self.find(board, i - 1, j, trie[board[i][j]])
            self.find(board, i, j - 1, trie[board[i][j]])
            self.used[i][j] = False

words = ["oath","pea","eat","rain","oak","ath","kae","ner"] 
board =[  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']]
len(board)
board[0][0]
board[1]
type(words)
type(board)
l=Solution()
l.findWords(board,words)
