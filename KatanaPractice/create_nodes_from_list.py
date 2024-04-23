nodeTypes = ["PrimitiveCreate", "AttributeSet", "GafferThree", "Render"]
prevN = None
for i,t in enumerate(nodeTypes):
    n = NodegraphAPI.CreateNode(t,rootNode)
    NodegraphAPI.SetNodePosition(n, (300, -i*75 - 100))
    if prevN:
        outputPort = prevN.getOutputPortByIndex(0)
        inputPort = n.getInputPortByIndex(0)
        outputPort.connect(inputPort)
    prevN = n