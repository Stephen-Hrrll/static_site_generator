import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_initialization(self):
        node = HTMLNode(tag="p", value="Hello", children=None, props={"class": "text"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"class": "text"})

        # Test default values
        node_default = HTMLNode()
        self.assertIsNone(node_default.tag)
        self.assertIsNone(node_default.value)
        self.assertEqual(node_default.children, [])
        self.assertEqual(node_default.props, {})

    def test_repr(self):
        node = HTMLNode(tag="a", value="Click here", children=[], props={"href": "https://example.com"})
        expected_repr = "tag=a value=Click here children=None props={'href': 'https://example.com'}"
        self.assertEqual(repr(node), expected_repr)

    def test_props_to_html(self):
        node = HTMLNode(tag="div", value="Test", props={"id": "main", "class": "container"})
        expected_props_html = "tag=div value=Test children=None props={'id': 'main', 'class': 'container'}"
        self.assertEqual(node.props_to_html(), expected_props_html)

if __name__ == '__main__':
    unittest.main()
