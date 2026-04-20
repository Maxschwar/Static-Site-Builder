import unittest
from htmlnode import HtmlNode

node1 = HtmlNode("p","Hello world!")
node2 = HtmlNode("a", "link text to boot", None, { "href": "http://www.boot.dev", "target": "_blank"})
node3 = HtmlNode("a", "link text to boot", None, { "href": "http://www.boot.dev", "target": "_blank"})
node4 = HtmlNode("h1", "Welcome to my site", [node1,node2])

class TestHtmlNode(unittest.TestCase):
    def test_repr(self):
        self.assertEqual(node2.__repr__(), node3.__repr__())
        self.assertNotEqual(node1.__repr__(), node2.__repr__())
        self.assertEqual(node4.__repr__(), node4.__repr__())

if __name__ == "__main__":
    unittest.main()