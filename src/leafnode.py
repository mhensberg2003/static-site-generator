from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value")
        if not self.tag:
            return self.value
        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            html = f"<{self.tag}"
            for key, value in self.props.items():
                html += f" {key}=\"{value}\""
            html += f">{self.value}</{self.tag}>"
            return html
        
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"