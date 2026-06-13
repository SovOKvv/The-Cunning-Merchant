from circular_list import CircularLinkedList


class MerchantTask:
    def __init__(self, n: int, m: int, k: int):
        self.n = n
        self.m = m
        self.k = k
        self.total_bales = 2 * n
        self.circle = CircularLinkedList()
        self.generate_cargo_circle()

    def generate_cargo_circle(self):
        for i in range(1, self.total_bales + 1):
            self.circle.append(i)

    def find_safe_positions(self) -> list:
        current = self.circle.head
        prev = self.circle.tail

        for _ in range(self.m - 1):
            prev = current
            current = current.next

        for _ in range(self.n):
            for _ in range(self.k):
                prev = current
                current = current.next

            self.circle.remove_after(prev)
            current = prev.next

        return sorted(self.circle.get_all_values())