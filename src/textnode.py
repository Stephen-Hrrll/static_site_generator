from enum import Enum

class TextType(Enum):
    NORMAL = "Normal Text"
    BOLD = "Bold Text"
    ITALIC = "Italic Text"
    CODE = "Code Text"
    LINKS = "Links"
    IMAGES = "Images"



class TextNode:
    def __init__(self, text, text_type:TextType , url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        text = self.text == other.text
        tType = self.text_type == other.text_type
        url = self.url == other.url

        if (text and tType) and url:
            return True
        
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"