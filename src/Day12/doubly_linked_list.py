from __future__ import annotations

from typing import Generic, TypeVar

T = TypeVar("T")  # Declare a type variable


class ListNode(Generic[T]):  # noqa: UP046
    def __init__(
        self,
        value: T,
        nprev: ListNode[T] | None = None,
        nnext: ListNode[T] | None = None,
    ) -> None:
        self.value = value
        self.nprev: ListNode[T] | None = nprev
        self.nnext: ListNode[T] | None = nnext


class DoublyLinkedList(Generic[T]):  # noqa: UP046
    def __init__(self) -> None:
        self.length: int = 0
        self.head: ListNode[T] | None
        self.tail: ListNode[T] | None = None

    def prepend(self, item: T) -> None:
        node = ListNode(item)
        self.length += 1

        if not self.head:
            self.head = self.tail = node
            return

        node.nnext = self.head
        self.head.nprev = node
        self.head = node

    def insert_at(self, item: T, idx: int) -> None:
        if idx > self.length:
            raise IndexError("Index out of bounds")

        if idx == self.length:
            self.append(item)
            return

        if idx == 0:
            self.prepend(item)
            return

        curr = self._get_node_at(idx)
        node = ListNode(item)

        self.length += 1

        node.nnext = curr
        node.nprev = curr.nprev if curr else None

        if curr and curr.nprev:
            curr.nprev.nnext = node

        if curr:
            curr.nprev = node

    def append(self, item: T) -> None:
        node = ListNode(item)

        self.length += 1

        if not self.tail:
            self.head = self.tail = node
            return

        node.nprev = self.tail
        self.tail.nnext = node
        self.tail = node

    def remove(self, item: T) -> T | None:
        curr = self.head

        for _ in range(self.length):
            if not curr:
                continue

            if curr.value == item:
                break

            curr = curr.nnext

        if not curr:
            return None

        return self._remove_node(curr)

    def get(self, idx: int) -> T | None:
        node = self._get_node_at(idx)
        return node.value if node else None

    def remove_at(self, idx: int) -> T | None:
        node = self._get_node_at(idx)

        if not node:
            return None

        return self._remove_node(node)

    def _remove_node(self, node: ListNode[T]) -> T | None:
        self.length -= 1

        if self.length == 0:
            self.head = self.tail = None
            return node.value

        if node.nprev:
            node.nprev.nnext = node.nnext

        if node.nnext:
            node.nnext.nprev = node.nprev

        if node == self.head:
            self.head = node.nnext

        if node == self.tail:
            self.tail = node.nprev

        node.nnext = node.nprev = None

        return node.value

    def _get_node_at(self, idx: int) -> ListNode[T] | None:
        if (idx < 0) or (idx >= self.length):
            return None

        curr = self.head
        for _ in range(idx):
            if curr:
                curr = curr.nnext
        return curr
