
#Author:Gabriel Venegas
#Github:GVenegas1
#Date: Feb 18,2026
#Description:This program creates a linked list data structure that can add,
#remove,insert,search,and reverse a list of nodes using recursion

class Node:
    """Represents a single node in the linked list"""

    def __init__(self, data):
        #this is the value we are storing
        self.data = data
        #this will point to the next node
        self.next = None


class LinkedList:
    """A linked list class that uses recursion"""
    def __init__(self):
        # when we first make the list there are no nodes so head is 'None'
        self._head = None


    def get_head(self):
        """Returns the first node in the list"""
        # just gives back whatever the head is pointing to
        return self._head


    def is_empty(self):
        """Returns True if the list is empty"""
        #if head is 'None' that means there are no nodes at all
        return self._head is None


    def add(self, value):
        """Adds a new value to the end of the list"""
        if self._head is None:
            #the list is empty so we can just make the first node here
            self._head = Node(value)

        else:
            # the list has stuff so we need to find the end first
            self._add_help(self._head, value)


    def _add_help(self, node,value):
        """Recursively finds the last node and adds after it"""
        #we keep going until we find a node where next is 'None'
        if node.next is None:

            #we found the last node so we attach the new node
            node.next = Node(value)
        else:
            # call the same function on the next node
            self._add_help(node.next, value)


    def remove(self, value):
        """Removes the first node with the given value"""
        #this handles the case where we delete the head node/becomes new head
        self._head = self._rem_help(self._head, value)


    def _rem_help(self, node, value):
        """Searches for the value and removes it"""
        if node is None:
            #we went through the whole list & just return 'None' and nothing changed
            return None

        if node.data == value:
            #found the node we want to delete

            return node.next
        #whatever the helper returns becomes this nodes new next
        node.next = self._rem_help(node.next, value)
        return node

    def contains( self, value):
        """Return True if the value is in the list"""
        return self._con_help(self._head, value)


    def _con_help( self,node, value):
        """Searches the list for the value"""
        if node is None:

            #we reached the end of the list without finding it
            return False
        if node.data ==value:

            # this node has the value we are looking for
            return True

        #not found yet so we check the next node by calling the function again
        return self._con_help(node.next, value)


    def insert( self,value,position):
        """Inserts a value at the given index in the list"""
        #the helper returns the updated list so we save it back to head
        self._head = self._ins_help( self._head, value,position)


    def _ins_help(self, node,value, position):
        """Recurs walks to the right position"""
        if position <= 0 or node is None:

            #either count down to the right spot or just put it at the end
            new_node = Node(value)

            #the new node points to whatever was here before
            new_node.next = node
            return new_node

        #move to the next node and sub:1 from pos each time, so we know when to stop
        node.next = self._ins_help(node.next, value, position - 1)
        return node


    def reverse(self):
        """reverse the order of the list"""
        #the helper gives us back the new head after flipping everything
        self._head = self._rev_help(self._head)


    def _rev_help(self,node):
        """Recurs reverses the direction of each pointer"""
        if node is None or node.next is None:
            # return if the list is empty or we only have one node
            return node

        #go all the way to the end of the list first before we start flipping
        new_head = self._rev_help(node.next)

        # now we flip the pointer
        node.next.next =node
        node.next= None

        #keep passing the new head all the way back up
        return new_head



    def to_plain_list(self):
        """Converts the linked list into a normal python list"""
        #start from the head and let the helper build the list
        return self._list_help(self._head)

    def _list_help(self, node):
        """Recurs builds and returns a plain python list"""
        if node is None:
            #end of list/return an empty list
            return []
        #take this nodes data and put it in a list and adds next node
        return [node.data] + self._list_help(node.next)