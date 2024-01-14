class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

# Example usage:
trie = Trie()
words = ["apple", "banana", "orange", "grape", "pear"]

# Insert words into the Trie
for word in words:
    trie.insert(word)

# Search for words in the Trie
search_word = "orange"
if trie.search(search_word):
    print(f"{search_word} found in the Trie")
else:
    print(f"{search_word} not found in the Trie")
