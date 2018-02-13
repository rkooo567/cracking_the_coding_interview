# Tries: Contacts

**1. First approach**: I tried searching words using the class Contacts that saves the list of words that are added. It took so much time to complete the process

**2. Second approach**: I created a word tree that saves the letter in a tree format. I used the recursion to find the number of children of the node for the search function. It failed tests because it took so much time to check the number of children of nodes. 

**3. final approach**: I added the attribute named size that tracked the number of child of nodes. Whenever the new word was added as a child, I increased size, so when I actually searched the number of children of query word, I didn't need to have the seperate function, num_child(root) that used recursion. It reduced a lot of time to execute the program. 