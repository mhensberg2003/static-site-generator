import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_constructor(self):
        node = HTMLNode("a", "hello", [HTMLNode("h1", "heading", None, None)], {"href": "https://www.google.com"})
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, "hello")
        self.assertListEqual(node.children, [HTMLNode("h1", "heading", None, None)])
        self.assertEqual(node.props, {"href": "https://www.google.com"})
        

    def test_eq(self):
        node = HTMLNode("a", "hello", [HTMLNode("h1", "heading", None, None)], {"href": "https://www.google.com"})
        node2 = HTMLNode("a", "hello", [HTMLNode("h1", "heading", None, None)], {"href": "https://www.google.com"})
        nodeDifferentTag = HTMLNode("p", "hello", [HTMLNode("h1", "heading", None, None)], {"href": "https://www.google.com"})
        nodeDifferentValue = HTMLNode("a", "hey", [HTMLNode("h1", "heading", None, None)], {"href": "https://www.google.com"})
        nodeDifferentChildren = HTMLNode("a", "hello", None, {"href": "https://www.google.com"})
        nodeDifferentProps = HTMLNode("a", "hello", [HTMLNode("h1", "heading", None, None)], None)
        self.assertEqual(node, node2)
        self.assertNotEqual(node, nodeDifferentTag)
        self.assertNotEqual(node, nodeDifferentValue)
        self.assertNotEqual(node, nodeDifferentChildren)
        self.assertNotEqual(node, nodeDifferentProps)
        self.assertIsInstance(node, HTMLNode)
        
    def test_repr(self):
        node = HTMLNode("a", "hello", [HTMLNode("h1", "heading", None, None)], {"href": "https://www.google.com"})
        self.assertIn("HTMLNode(a, hello", repr(node))
        self.assertIn("[HTMLNode(", repr(node))
        self.assertIn("{\'href\': ", repr(node))
        self.assertIsInstance(repr(node), str)

if __name__ == "__main__":
    unittest.main()