#
# Name:
#

from Proj2_tree import printTree

#
# The following two trees are useful for testing.
#
smallTree = \
    ("Is it bigger than a breadbox?",
        ("an elephant", None, None),
        ("a mouse", None, None))
mediumTree = \
    ("Is it bigger than a breadbox?",
        ("Is it gray?",
            ("an elephant", None, None),
            ("a tiger", None, None)),
        ("a mouse", None, None))

def main():
    """DOCSTRING!"""
    # Write the "main" function for 20 Questions here.  Although
    # main() is traditionally placed at the top of a file, it is the
    # last function you will write.
    print("Welcome to 20 Questions!")
    
    if yes("Would you like to load a tree from a file?"):
        response = input("What's the name of the file?")
        treeFile = open(response, "r")
        tree = loadTree(treeFile)
        treeFile.close
        newTree = play(tree)
    else:
        tree = ("Is it bigger than a breadbox?", ("an elephant", None, None), ("a mouse", None, None))
        newTree = play(tree)
    
    if yes("Would you like to play again?"):
        newTree = play(newTree)
    else:
        if yes("Would you like to save the file?"):
            response = input("What's the name of the file?")
            treeFile = open(response, "w")
            saveTree(newTree, treeFile)
            treeFile.close()

def isLeaf(tree):
    if tree[1:] == (None, None): 
        return True
    return False

def yes(prompt):
    response = input(prompt)
    if response in ['yes', "y", "yup", "sure"]:
        return True
    return False

def playLeaf(tree):
    return tree[0], yes(f"Is it {tree[0]}?")

def simplePlay(tree):
    """DOCSTRING!"""
    """This function accepts a single argument, which is a tree (or a sub-part of a tree), 
    and plays the game once by using the tree to guide its questions. 
    It returns True if the computer guessed the answer."""
    if isLeaf(tree) == True:
        return playLeaf(tree)[1]
    else:
        if yes(tree[0]) == True:
            return simplePlay(tree[1])
        else:
            return simplePlay(tree[2])

def get_true(tree):
    print("I got it!")
    return tree

def get_false(tree, object):
    question = input(f"What's a question that distinguishes between {object} and {tree[0]}?")
    if yes(f"And what's the answer for {object}?") == True:
        return (question, (object, None, None), tree)
    else:
        return ((question, tree, (object, None, None)))

    
def play(tree):
    """DOCSTRING!"""
    """this function accepts a single argument, which is a tree, 
    and plays the game once by using the tree to guide its questions. 
    However, instead of returning just True or False, 
    play returns a new tree that is the result of playing the game 
    on the original tree and learning from the answers."""

    if isLeaf(tree) == True:
        if simplePlay(tree) == True:
            return get_true(tree)
        else: 
            object = input("Drats! What was it?")
            return get_false(tree, object)
    else:
        if yes(tree[0]) == True:
            return (tree[0], play(tree[1]), tree[2])
        else:
            return (tree[0], tree[1], play(tree[2]))



def saveTree(tree, treeFile):
    if isLeaf(tree):
        print("Leaf", file = treeFile)
        print(tree[0], file = treeFile)
    else:
        print("Internal node", file = treeFile)
        print(tree[0], file = treeFile)
        saveTree(tree[1], treeFile)
        saveTree(tree[2], treeFile)


def loadTree(treeFile):
    line = treeFile.readline()
    if line.strip() == "Leaf":
        line = treeFile.readline()
        return (line.strip(), None, None)
    elif line.strip() == "Internal node":
        line = treeFile.readline()
        return (line.strip(), loadTree(treeFile), loadTree(treeFile))




            
#
# The following two-line "magic sequence" must be the last thing in
# your file.  After you write the main() function, this line it will
# cause the program to automatically play 20 Questions when you run
# it.
#
if __name__ == '__main__':
    main()
