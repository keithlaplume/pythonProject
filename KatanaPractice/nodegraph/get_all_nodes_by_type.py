materialNodes = NodegraphAPI.GetAllNodesByType("Material")

for n in materialNodes:
    nodeName = n.getName()
    namespaceValue = n.getName()
    if namespaceValue == "":
        print("The node {} has no namespace".format(nodeName))
    else:
        print("The node {} has namespace {}".format(nodeName, namespaceValue))