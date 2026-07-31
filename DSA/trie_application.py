class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Stores the word when reaching an end node

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        # 1. Build the Trie
        root = TrieNode()
        for word in words:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = word

        ROWS, COLS = len(board), len(board[0])
        res = []

        # 2. DFS / Backtracking Function
        def dfs(r, c, parent_node):
            char = board[r][c]
            curr_node = parent_node.children[char]

            # If we found a word, add to results and clear it to prevent duplicates
            if curr_node.word:
                res.append(curr_node.word)
                curr_node.word = None

            # Mark cell as visited
            board[r][c] = "#"

            # Explore all 4 directional neighbors
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] in curr_node.children:
                    dfs(nr, nc, curr_node)

            # Backtrack
            board[r][c] = char

            # Optimization: Prune leaf nodes from the Trie to reduce work
            if not curr_node.children:
                parent_node.children.pop(char)

        # 3. Start DFS from every cell matching a top-level letter in the Trie
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in root.children:
                    dfs(r, c, root)

        return res