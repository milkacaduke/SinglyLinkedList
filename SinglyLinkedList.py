
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
			newNode = LLNode(data)
			newNode.next = self.head
			self.head = newNode
		else:
			self.head = LLNode(data)


	def insert_tail(self, data):
		if self.head is None:
			newNode = LLNode(data)
			self.head = newNode
			return

		curNode = self.head
		while curNode.next:
			curNode = curNode.next

		curNode.next = LLNode(data)


	def insert_after_node(self, prevNode, data):
		if self.head is None:
			print("Linked List empty")
			return

		if prevNode is None:
			print("prevNode provide is None")
			return

		newNode = LLNode(data)
		newNode.next = prevNode.next
		prevNode.next = newNode


	def insert_after_data(self, prevNodeData, data):
		if prevNodeData is None:
			print("prevNode data provided is None")
			return

		if self.head is None:
			print("Linked List empty")
			return

		curNode = self.head
		while curNode:
			curData = curNode.data
			if curData == prevNodeData:
				return self.insert_after_node(curNode, data)
			curNode = curNode.next

		print("No node with {} in Linked List".format(prevNodeData))


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

	def delete_at_index(self, idx):
		print("delete_at_index {}".format(idx))
		if idx is None:
			print("index not provided")
			return

		if idx < 0:
			print("index provided invalid")
			return

		if self.head is None:
			print("Linked List empty")
			return

		if idx == 0 and self.head.next is None: # special case remove at head and LL only one node
			self.head = None
			return

		i = 0
		curNode = self.head
		prevNode = None

		while curNode:
			if i == idx:
				if prevNode is None: # remove at head
					# we could just call self.delete_head()
					temp = self.head
					self.head = self.head.next
					return temp
				else:
					prevNode.next = curNode.next
					return curNode
			i += 1
			prevNode = curNode
			curNode = curNode.next

		print("index provided is out of bounds")
		return






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

		# print head arrow, style stuff not important
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


# # main
ll = LinkedList()

ll.insert('A')
ll.insert('B')
# ll.insert('C')
# ll.insert('D')
# ll.insert('E')
# # print(ll.head.data)

ll.printAll()

ll.printAll()


# ll.insert_after_data('E', 'E1')
# ll.insert_after_data('C', 'C1')
# ll.insert_after_data('B', 'B1')
# ll.printAll()

# print("length: {}".format(ll.length()))
# ll.delete_tail()
# ll.printAll()
