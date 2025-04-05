import unittest

from leafnode import LeafNode

class TestTextNode(unittest.TestCase):

    def test_constructor(self):
        p_node = LeafNode("p", "Hello, world!")
        a_node = LeafNode("a", "Hello again!", {"href": "https://udenusa.dk"})
        self.assertEqual(p_node.to_html(), "<p>Hello, world!</p>")
        self.assertEqual(a_node.to_html(), "<a href=\"https://udenusa.dk\">Hello again!</a>")

    def test_eq(self):
        p_node = LeafNode("p", "Hello, world!")
        p_node2 = LeafNode("p", "Hello, world!")
        nodeDifferentTag = LeafNode("h1", "Hello, world!")
        nodeDifferentValue = LeafNode("p", "Roger sir!")
        nodeDifferentProps = LeafNode("p", "Hel´lo, world!", {"href": "https://vocata.app"})
        self.assertEqual(p_node, p_node2)
        self.assertNotEqual(p_node, nodeDifferentTag)
        self.assertNotEqual(p_node, nodeDifferentValue)
        self.assertNotEqual(p_node, nodeDifferentProps)
        self.assertIsInstance(p_node, LeafNode)

    def test_repr(self):
        p_node = LeafNode("p", "Hello, world!")
        a_node = LeafNode("a", "Hello again!", {"href": "https://udenusa.dk"})
        self.assertEqual(repr(p_node), "LeafNode(p, Hello, world!, None)")
        self.assertEqual(repr(a_node), "LeafNode(a, Hello again!, {'href': 'https://udenusa.dk'})")
        self.assertIsInstance(repr(p_node), str)

if __name__ == "__main__":
    unittest.main()