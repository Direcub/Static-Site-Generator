import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode



class TestLeafNode(unittest.TestCase):
    def test_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_no_tag(self):
        node = LeafNode(None, "this is a value", None)
        assert node.to_html() == "this is a value"

    def works_at_all(self):
        node = LeafNode("p", "this is a value", None)
        assert node.to_html() == "<p>this is a value</p>"

if __name__ == "__main__":
    unittest.main()