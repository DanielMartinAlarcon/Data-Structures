Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?

        O(1)

2. What is the runtime complexity of `dequeue`?

        O(1)

3. What is the runtime complexity of `len`?

        O(1)

## Binary Search Tree

1. What is the runtime complexity of `insert`? 

        O(log(n)), because at each intersection we're eliminating half of the tree from the list of nodes that we have to evaluate.  This assumes a balanced tree.  If it's grossly imbalanced, we might have to evaluate as many as O(n) items.

2. What is the runtime complexity of `contains`?

        O(log(n)), see above.

3. What is the runtime complexity of `get_max`? 

        O(log(n)), see above.

## Heap

1. What is the runtime complexity of `_bubble_up`?

        On a balanced tree, it should be O(log(n)), as we only have to evaluate one lineage between parent and leaf (so it's like we're going in the opposite direction, which we also know to be O(log(n))).  In the worst case of a completely unbalanced tree, however, complexity would be O(n).

2. What is the runtime complexity of `_sift_down`?

        O(n), because in this case we have to evaluate all the nodes in the tree.

3. What is the runtime complexity of `insert`?

        Same as `_bubble_up`, so O(log(n))

4. What is the runtime complexity of `delete`?

        Same as `_sift_down`, so O(n)

5. What is the runtime complexity of `get_max`?

        O(1).  That's the beauty of heaps.

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?

        O(1)

2. What is the runtime complexity of `ListNode.insert_before`?

        O(1)

3. What is the runtime complexity of `ListNode.delete`?

        O(1)

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?

        O(1)

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?

        O(1)

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?

        O(1)

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?

        O(1)

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?

        O(1)

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?

        O(1)

10. What is the runtime complexity of `DoublyLinkedList.delete`?

        O(1)

a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

    In the worst case, `Array.splice` has a complexity of `O(n)`, because it has to shift over each element by one place. With a DLL, on the other hand, we just have to shift a couple of references.  The DLL should generally perform better for any of these operations.  Finding particular items in the list, however, is another matter.