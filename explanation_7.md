Explanations to problem 7 - HTTP Router Trie

I use the similar concepts used in Trie chapter and Autocomplete question to
create a RouteTrieNode class and RouteTrie class. Since router's main purpose is
to return handler, I replaced "end of word" constructor in those class with handler
constructor. The Router has an input of root_handler, so the router can return
home page if it wants to. The Router class wraps around RouteTrie class. There're
3 methods - lookup, add_handler and split_path within the Router class. The split_path
method splits the http path into parts, and is applied in 2 other methods to help
lookup/add handler.

In the worst case, the run time of this problem will take O(k * n) time, and since
I don't use recursive method, so the space is using only O(1) space. In my mind, 
this is efficient and space-saving.
