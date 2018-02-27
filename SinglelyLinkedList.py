
class LLNode(object):
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList(object):
	def __init__(self):
		self.head = None

	def insert(self, data):
		if data is not None:
			self.insert_head(data)

	def insert_head(self, data):
		if self.head:
			new_node = LLNode(data)
			new_node.next = self.head
			self.head = new_node
		else:
			self.head = LLNode(data)

	def insert_tail(self, data):
		if self.head is None:
			print("Linked List empty")
			return False

		curNode = self.head
		while curNode.next:
			curNode = curNode.next

		curNode.next = LLNode(data)

	def delete_head(self):
		if self.head is None:
			print("Linked List empty, cannot preform delete")
			return False

		temp = self.head
		self.head = self.head.next
		return temp

	def delete_tail(self):
		if self.head is None:
			print("Linked List empty, cannot preform delete")
			return False

		curNode = self.head
		prevNode = None
		while curNode.next:
			prevNode = curNode
			curNode = curNode.next
		
		prevNode.next = None
		return curNode

	def length(self):
		if self.head is None:
			return 0

		cur = self.head
		count = 0
		while cur:
			count += 1
			cur = cur.next
		return count

	def printAll(self):
		if self.head is None:
			print("Linked List empty!")

		curNode = self.head

		# print head arrow
		print("")
		print("[head]")
		print("   v")
		print("   ", end="")


		while curNode:
			if curNode.next is None:
				print(curNode.data)
				print("")
			else:	
				print(curNode.data + " -> ", end="")
			curNode = curNode.next









# main
ll = LinkedList()

ll.insert('A')
ll.insert('B')
ll.insert('C')
ll.insert('D')
ll.insert('E')
ll.insert_tail('F')
# print(ll.head.data)

ll.printAll()
print("length: {}".format(ll.length()))
ll.delete_tail()
ll.printAll()
