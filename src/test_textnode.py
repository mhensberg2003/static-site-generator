import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):

    def test_constructor(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "test.com")
        self.assertEqual(node.text, "This is a text node")
        self.assertEqual(node.text_type, TextType.BOLD)
        self.assertIsNone(node.url)
        self.assertEqual(node2.text, "This is a text node")
        self.assertEqual(node2.text_type, TextType.BOLD)
        self.assertEqual(node2.url, "test.com")

    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        nodeDifferentText = TextNode("This is another text node", TextType.BOLD)
        nodeDifferentTextType = TextNode("This is a text node", TextType.LINK)
        nodeDifferentURL = TextNode("This is a text node", TextType.BOLD, "test.com")
        self.assertEqual(node, node2)
        self.assertNotEqual(node, nodeDifferentText)
        self.assertNotEqual(node, nodeDifferentTextType)
        self.assertNotEqual(node, nodeDifferentURL)
        self.assertIsInstance(node, TextNode)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "test.com")
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, None)")
        self.assertEqual(repr(node2), "TextNode(This is a text node, bold, test.com)")
        self.assertIsInstance(repr(node), str)


if __name__ == "__main__":
    unittest.main()