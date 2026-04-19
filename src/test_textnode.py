import unittest

from textnode import TextNode, TextType

node1 = TextNode("This is a text node", TextType.PLAIN)
node2 = TextNode("This is a text node", TextType.PLAIN, None)
node3 = TextNode("This is a bold text node", TextType.BOLD) 
node4 = TextNode("This is a italic text node", TextType.ITALIC)
node5 = TextNode("This is a italic text node", TextType.ITALIC)
node6 = TextNode("This is a text node", TextType.LINK, "http://https:www.boot.dev")
node7 = TextNode("This is a text node", TextType.ITALIC)

class TestTextNode(unittest.TestCase):
    def test_eq(self):        
        self.assertNotEqual(node1, node7)
        self.assertNotEqual(node1, node3)
        self.assertEqual(node4, node5)
        self.assertEqual(node1, node2)

    def test_repr(self):
        self.assertEqual(node1.__repr__(), "TextNode(This is a text node, plain, None)")
        self.assertEqual(node2.__repr__(), "TextNode(This is a text node, plain, None)")
        self.assertNotEqual(node3.__repr__(), "TextNode(This is a text node, plain, None)")
        self.assertNotEqual(node1.__repr__(), "TextNode(This is a text node, plain)")



if __name__ == "__main__":
    unittest.main()