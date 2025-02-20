from xml.dom import minidom

root = minidom.Document()
listaFamilie = root.createElement("lista_nume_familie")
root.appendChild(listaFamilie)

# Elementul 1
e1 = root.createElement("numeFamilie")
e1.setAttribute("lungime", "6")
e1.setAttribute("consoane", "2")
e1.setAttribute("vocale", "4")
e1.setAttribute("diacritice", "0")
nodText1 = root.createTextNode("Abunei")
e1.appendChild(nodText1)
listaFamilie.appendChild(e1)

# Elementul 2
e2 = root.createElement("numeFamilie")
e2.setAttribute("lungime", "7")
e2.setAttribute("consoane", "3")
e2.setAttribute("vocale", "4")
e2.setAttribute("diacritice", "1")
nodText2 = root.createTextNode("Abălaru")
e2.appendChild(nodText2)
listaFamilie.appendChild(e2)

xml_string = root.toprettyxml(indent="\t")
file = "numeFamilie.xml"
with open(file, "w", encoding="utf-8-sig") as f:
    f.write(xml_string)
    f.close()
