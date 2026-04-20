import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):    
        
        node1 = LeafNode("p", "Hello, world!")
        node2 = LeafNode("a", "Come to boots!", { "href": "https://www.boot.dev"})

        self.assertEqual(node1.to_html(), "<p>Hello, world!</p>")
        self.assertEqual(node2.to_html(), "<a href=\"https://www.boot.dev\">Come to boots!</a>")
        self.assertNotEqual(node1, node2)

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")


    def test_values(self):
        
        node = LeafNode("a", "This is a Link to boot.dev", { "href":"https://www.boot.dev", "target": "_blank"})

        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, "This is a Link to boot.dev")
        self.assertEqual(node.children, None)
        self.assertNotEqual(node.props, None)

if __name__ == "__main__":
    unittest.main()

