import sys


# code for a depth-first search and stack (last-in, first-out)
class Node:  # defined a class to keep track of the below parameters
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier:  # stores all frontier data
    def __init__(self):  # creates a frontier and stores date in the list
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)  # appends to end of the list

    def contains_state(self, state):  # checks if the frontier contains a particular state
        return any(node.state == state for node in self.frontier)

    def empty(self):  # checks if the list is empty
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:  # last-in, first-out. removes the last item added
            node = self.frontier[-1]  # last item
            self.frontier = self.frontier[:-1]  # removes the node
            return node


# code for breadth-first search and queue (first-in, first-out)
class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:  # first-in, first-out. removes the first item added
            node = self.frontier[0]  # first item
            self.frontier = self.frontier[1:]  # removes the node
            return node

