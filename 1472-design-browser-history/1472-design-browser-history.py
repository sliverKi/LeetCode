class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
        

class BrowserHistory:
    def __init__(self, homepage: str):
        self.cur = ListNode(homepage)
            
    def visit(self, url: str) -> None:
        self.cur.next = ListNode(url, self.cur)
        #Node의 prev값을 이전에 생성한 노드로 설정후, 이전에 생성한 노드의 next를 새 노드와 연결함.
        self.cur = self.cur.next
        #새로 생성된 node를 현재노드로 갱신

    def back(self, steps: int) -> str:
        while self.cur.prev and steps > 0:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.val

    def forward(self, steps: int) -> str:
        while self.cur.next and steps > 0:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.val