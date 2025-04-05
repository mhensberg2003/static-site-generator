from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        # If tag is missing or value is missing in one of the children, throw ValueError
        if not self.tag:
            raise ValueError("ParentNode must have a tag")
        if not self.children or len(self.children) == 0:
            raise ValueError("ParentNode must have children")
            
        # Build opening tag with props
        html = f"<{self.tag}"
        if self.props:
            for key, value in self.props.items():
                html += f' {key}="{value}"'
        html += ">"

        # Recursively render all children
        for child in self.children:
            html += child.to_html()

        # Add closing tag to html string
        html += f"</{self.tag}>"
        return html
    
    def __repr__(self):
        return f"ParentNode(tag={repr(self.tag)}, children={repr(self.children)}, props={repr(self.props)})"
