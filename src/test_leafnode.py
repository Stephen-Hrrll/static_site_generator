import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_tag_with_value(self):
        node = LeafNode("p", "This is a paragraph of text.")
        expected = "<p>This is a paragraph of text.</p>"

        self.assertEqual(node.to_html(), expected)

    def test_with_props(self):
        node = LeafNode("a", "Click me!", {"href":"https://www.google.com"})

        expected = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), expected)

    def test_to_html_ValueError(self):
        node = LeafNode("a", None)
        self.assertRaises(ValueError, node.to_html)
    
    def test_to_html_no_tag(self):
        node = LeafNode(None, "Just raw text.")
        self.assertEqual(node.to_html(), "Just raw text.")

if __name__ == "__main__":
    unittest.main()

