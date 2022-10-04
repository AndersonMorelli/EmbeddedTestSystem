'''aaaa
bbbb
Wait(ms):
111
ccccc
Enviar serial:
jk
Saída Digital:
1:1
ddddd
Wait(ms):
100
Enviar serial:
asd
Saída Digital:
11:1
Entrada digital:
1:0'''


import xml.etree.cElementTree as ET

root = ET.Element("teste")
doc = ET.SubElement(root, "TC")

ET.SubElement(doc, "field1", name="blah").text = "some value1"
ET.SubElement(doc, "field2", name="asdfasd").text = "some vlaue2"

tree = ET.ElementTree(root)
tree.write("filename.xml")