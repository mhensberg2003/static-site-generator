class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag  # A streing representing the HTML tag name
        self.value = value # A string representing the value of the HTML tag
        self.children = children #A list of HTMLNode objects representing the children of this node
        self.props = props #A dict of key-value pairs representing the attributes of the HTML tag

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        finalString = ""
        for key, value in self.props.items():
            finalString += f"{key}={value} "
        return finalString
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def __eq__(self, other):
        if type(self) is not type(other):
            return False
        if (self.tag == other.tag) and (self.value == other.value) and (self.children == other.children) and (self.props == other.props):
            return True
        return False