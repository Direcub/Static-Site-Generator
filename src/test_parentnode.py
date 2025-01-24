import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_functioning(self):
        node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)
        assert node.to_html() == "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"

    def test_nesting(self):
        node = ParentNode("p", [LeafNode("b","Bold text"), ParentNode("p", [LeafNode(None, "Normal text"), LeafNode("i", "italic text")]), LeafNode(None, "Normal text")])
        assert node.to_html() == "<p><b>Bold text</b><p>Normal text<i>italic text</i></p>Normal text</p>"

if __name__ == "__main__":
    unittest.main()