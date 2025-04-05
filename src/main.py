from textnode import TextNode, TextType
from htmlnode import HTMLNode
def main():
    new_text = TextNode("This is some anchor text", TextType.LINK, "test.com")
    new_html = HTMLNode("a", "hello", [HTMLNode("h1", "heading", None, None)], {"href": "https://www.google.com"})

if __name__ == "__main__":
    main()