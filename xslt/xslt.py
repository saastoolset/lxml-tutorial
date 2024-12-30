from lxml import etree
import os

current_dir = os.path.dirname(__file__)

# Define the source XML
with open(os.path.join(current_dir, 'src.xml'), 'r') as file:
    source_xml = file.read()

# Define the XSLT
with open(os.path.join(current_dir, 'myxsl.xsl'), 'r') as file:
    xslt = file.read()

# Parse the XML and XSLT
source_doc = etree.XML(source_xml)
xslt_doc = etree.XML(xslt)

# Transform the XML with the XSLT
transform = etree.XSLT(xslt_doc)
result_tree = transform(source_doc)

# Print the result
print(str(result_tree))
