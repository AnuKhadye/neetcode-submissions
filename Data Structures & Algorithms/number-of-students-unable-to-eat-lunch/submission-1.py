from collections import deque

def take_sandwich(q, s):
    q.popleft()
    s.popleft()

def skipped_student(q):
    q.append(q.popleft())

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = deque(students)
        s = deque(sandwiches)

        skipped = 0
        
        while q:
            n = len(q)
            if skipped == n:
                return n

            if q[0] != s[0]:
                skipped_student(q)
                skipped += 1

            if q[0] == s[0]:
                take_sandwich(q, s)
                skipped = 0

        return len(q)

            









