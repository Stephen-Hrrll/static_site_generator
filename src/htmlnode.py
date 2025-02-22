class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag #A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        self.value = value #A string representing the value of the HTML tag (e.g. the text inside a paragraph)
        self.children = children #A list of HTMLNode objects representing the children of this node
        self.props = props #A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
        


    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
# end class HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(value=value,tag=tag, props=props, children=None)
        self.tag = tag #A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        self.value = value #A string representing the value of the HTML tag (e.g. the text inside a paragraph)
        self.props = props #A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}


    def to_html(self):
        if self.value == None:
            raise ValueError("all leaf nodes must have a value")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"
#end class LeafNode


