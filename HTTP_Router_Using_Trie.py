### HTTPRouter using a Trie
# A RouteTrie will store our routes and their associated handlers
#import re
class RouteTrie:
    def __init__(self, root_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.root.handler = root_handler

    def insert(self, path_list, handler_input):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        for path in path_list:
            if path not in current_node.children:
                current_node.children[path] = RouteTrieNode()
            current_node = current_node.children[path]
        current_node.handler = handler_input

    def find(self, path_list):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        for part in path_list:
            if part not in current_node.children:
                return None
            else:
                current_node = current_node.children[part]
        return current_node.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = None

    def insert(self, part):
        # Insert the node as before
        self.children[part] = RouteTrieNode()

# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.routetrie = RouteTrie(root_handler)

    def add_handler(self, path, handler_input):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_list = self.split_path(path)
        node = self.routetrie.insert(path_list, handler_input)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path_list = self.split_path(path)
        if self.routetrie.find(path_list) == None:
            return "Not found handler"
        return self.routetrie.find(path_list)

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and lookup functions,
        # so it should be placed in a function here
        path_list = path.split("/")
        length = len(path_list)
        if path_list[length-1] == "":
            path_list = path_list[:length-1]
        return path_list[1:]

# Here are some test cases and expected outputs you can use to test your implementation
# create the router and add a route
#router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router = Router("root handler")
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
# Edge cases:
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("https://classroom.udacity.com/nanodegrees/nd256/parts/da17de0f-f834-46f8-bb48-ee2705d95dc4/modules/bd252a0b-e9e7-473b-bcc1-bc7e3153568b/lessons/8ec390d0-e99d-44c0-88f9-f8f9faf467fc/project")) #Should print "Not found handler"
# Other cases:
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
