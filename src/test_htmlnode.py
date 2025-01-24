import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p", "test", None, {"is this good": "maybe"})
        node2 = HTMLNode("p", "test", None, {"is this good": "maybe"})
        htmlnode = node.props_to_html()
        htmlnode2 = node2.props_to_html()
        self.assertEqual(htmlnode, htmlnode2)
    
    def test_empty_props(self):
        empty = HTMLNode(props={})
        assert empty.props_to_html() == ""

    def test_single_props(self):
        node2 = HTMLNode(props={"class": "btn"})
        assert node2.props_to_html() == ' class="btn"'

if __name__ == "__main__":
    unittest.main()