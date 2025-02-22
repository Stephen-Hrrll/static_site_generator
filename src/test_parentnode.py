import unittest
from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_4_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"

        html_result= node.to_html()
        # print("html result:::::", html_result)
        self.assertEqual(html_result, expected)

    def test_child_with_props(self):
        node = ParentNode(
            "p",
            [
                LeafNode(None, "Please "),
                LeafNode("a", "Click me!", {"href": "https://www.google.com"})
            ]
        )

        expected = f'<p>Please <a href="https://www.google.com">Click me!</a></p>'

        self.assertEqual(node.to_html(), expected)

    def test_parent_with_props(self):
        node = ParentNode(
            "div",
            [
                LeafNode("h1", "Welcome"),
                LeafNode("p", "This is a paragraph."),
            ],
            {"class": "container", "id": "main"}
        )

        expected = '<div class="container" id="main"><h1>Welcome</h1><p>This is a paragraph.</p></div>'

        html_result= node.to_html()
        
        self.assertEqual(html_result, expected)

    #tests from solution files
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
        
    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )


    