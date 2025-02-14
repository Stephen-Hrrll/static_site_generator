class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag #A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        self.value = value #A string representing the value of the HTML tag (e.g. the text inside a paragraph)
        self.children = children #A list of HTMLNode objects representing the children of this node
        if self.children == None:
            self.children = list()
        self.props = props #A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
        if self.props == None:
            self.props = dict()


    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        return f"tag={self.tag} value={self.value} children={None if self.children == [] else self.children} props={self.props}"
    
    def __repr__(self):
        return self.props_to_html()
    
