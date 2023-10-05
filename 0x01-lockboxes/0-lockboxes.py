from collections import deque

def canUnlockAll(boxes):
    # Create a list to keep track of visited boxes
    visited = [False] * len(boxes)
    visited[0] = True  # Mark the first box as visited since it's unlocked
    queue = deque([0])  # Use a queue for BFS, start with the first box

    while queue:
        current_box = queue.popleft()
        # Check the keys in the current box
        for key in boxes[current_box]:
            if 0 <= key < len(boxes) and not visited[key]:
                # If the key opens a new box, mark it as visited and add it to the queue
                visited[key] = True
                queue.append(key)

    # Check if all boxes have been visited
    return all(visited)
