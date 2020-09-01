# AUTOGENERATED! DO NOT EDIT! File to edit: 02_utils.ipynb (unless otherwise specified).

__all__ = ['make_tree', 'strip_ns']

# Cell
import xml.etree.ElementTree as ET
from io import StringIO

# Cell
def make_tree(response):
    """Make an `ElementTree` from the text of an XML `response`"""
    tree = ET.iterparse(StringIO(response.text))
    return tree

def strip_ns(tree):
    """strip all the namespaces from `tree`"""
    for _, el in tree:
        _, _, el.tag = el.tag.rpartition('}') # strip ns#
    return tree