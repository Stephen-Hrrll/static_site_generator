import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.url.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.url.com")
        self.assertEqual(node, node2)
    
    def test_not_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.ur.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.url.com")
        self.assertNotEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This s a text node", TextType.BOLD, "www.url.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.url.com")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()