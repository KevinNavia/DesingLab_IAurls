from collections import deque
class UrlQueue:
    def __init__(self):
        self.queue = deque()
    def enqueue(self, url):
        self.queue.append(url)
    def dequeue(self):
        return self.queue.popleft() if self.queue else None
    def is_empty(self):
        return not self.queue
