class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    """
    Класс, реализующий структуру данных 'Циклический однонаправленный список'.

    В таком списке последний элемент (tail) всегда ссылается на первый (head),
    образуя замкнутое кольцо. Применяется для циклического обхода элементов.
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        """
        Добавляет новый элемент в конец циклического списка.

        :param value: Значение, которое необходимо сохранить в новом узле.
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head

    def remove_after(self, prev_node):
        """
        Удаляет узел, следующий сразу за переданным узлом prev_node.

        :param prev_node: Узел, после которого нужно произвести удаление.
        :return: Данные (data) удаленного узла.
        """

        if self.head == self.head.next:
            removed_value = self.head.data
            self.head = None
            self.tail = None
            return removed_value

        removed_node = prev_node.next
        prev_node.next = removed_node.next

        if removed_node == self.head:
            self.head = removed_node.next
        if removed_node == self.tail:
            self.tail = prev_node

        return removed_node.data

    def get_all_values(self):
        """
        Собирает данные всех узлов списка, проходя кольцо ровно один раз.

        :return: Список (list) со значениями всех элементов в порядке их следования,
                 либо пустой список, если структура не заполнена.
        """

        if not self.head:
            return []

        values = []
        current = self.head
        while True:
            values.append(current.data)
            current = current.next
            if current == self.head:
                break
        return values