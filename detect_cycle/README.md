# Detect Cycle

## First approach
I used tree recursion to detect the cycle. It was pretty inefficient.

## second approach
Created two pointers that point the next node and a after next node. Let's say the first one is called next and the second one is nextnext.
If in every loop, next is pointing next and nextnext is pointing the after next node, if there is a cycle in the linked list, 
it will eventually meet someday. That's the time when the loop is terminated and return true. 
