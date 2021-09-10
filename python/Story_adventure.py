######
# TREENODE CLASS
######
class TreeNode():
  def __init__(self, story_piece):
    self.story_piece = story_piece
    self.choices = []

  def add_child(self, node):
    self.choices.append(node)

 
  def traverse(self):
    story_node = self
    print(story_node.story_piece)
    while len(story_node.choices) > 0:
      choice = input("""Enter 1 or 2 to continue the story: """)
      if choice not in ["1","2"]:  
        print("Invalid Choice!")
      else:
        chosen_index = int(choice)
        chosen_index -= 1
        chosen_child = story_node.choices[chosen_index]
        print(chosen_child.story_piece)
        story_node = chosen_child
######
# VARIABLES FOR TREE
######
user_choice = input("What is your name? ")
print("\n ---Have a great adventure, "+ user_choice + "---")
ans = len(user_choice) * 10

story_root = TreeNode("""
You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you: 
1 ) Roar back!
2 ) Run to the left...
""")
choice_a = TreeNode("""
The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
""")
choice_a_1 = TreeNode("""
The bear returns and tells you it's been a rough week. After making peace with
a talking bear, he shows you the way out of the forest.
 
YOU HAVE ESCAPED THE WILDERNESS.
""")

choice_a_2 = TreeNode("""
The bear returns and tells you that bullying is not okay before leaving you alone
in the wilderness.
 
YOU REMAIN LOST.
""")

choice_b = TreeNode("""
You come across a clearing full of flowers. 
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
""")

choice_b_1 = TreeNode("""
The bear is unamused. After smelling the flowers, it turns around and leaves you alone.
 
Do you:
1 ) Follow the bear and ask for help. 
2 ) Smell the flower and wonder some more.
""")
choice_b_1_2 = TreeNode(""" 
The bear thinks on it, forgives you and say if you know what the number of your name times 10 is he will help you.

Is the anwser:
1) {0}
2) {1}
""".format(ans,ans*2))
choice_b_1_1 = TreeNode("""
You smelled the flowers some more, the bear has left and you remind lost in the woods forever """)

choice_b_2 = TreeNode("""
The bear understands and apologizes for startling you. Your new friend shows you a 
path leading out of the forest.
 
Do you:

1) Give the bear some honey for helping you out.
2) Take out a gun and shoot him at the end of the path.
""")
choice_b_2a = TreeNode(""" 
The bear was so happy with the jar of honey, he showed you where some hidden treasury was as he guided you out of the forest, you have made it out with lots of gold!!!""")
choice_b_2b = TreeNode("""
As soon as you have made it out, you shoot the bear, but didn't kill it, it got very angery and tore you apart, Now you are dead!!!""")

ans1 = TreeNode("""
The bear tells you its the correct answer and help you find you're way out of the forest!!! YAY!!
You win, {0}!!!! 
""".format(user_choice))
ans2 = TreeNode("""
The bear states that sadly you have gotten the answer incorrect, and has left you to find your way out of the forest, forever lost...""")

story_root.add_child(choice_a)
choice_a.add_child(choice_a_1)
choice_a.add_child(choice_a_2)


story_root.add_child(choice_b)
choice_b.add_child(choice_b_1)
choice_b_1.add_child(choice_b_1_2)
choice_b_1.add_child(choice_b_1_1)
choice_b.add_child(choice_b_2)
choice_b_2.add_child(choice_b_2a)
choice_b_2.add_child(choice_b_2b)
choice_b_1_2.add_child(ans1)
choice_b_1_2.add_child(ans2)
######
# TESTING AREA
######
print("Once upon a time...")
story_root.traverse()

