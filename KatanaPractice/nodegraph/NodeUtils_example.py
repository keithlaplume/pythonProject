from PackageSuperToolAPI import NodeUtils

nodeTypes =["PrimitiveCreate", "AttributeSet", "GafferThree", "Render"]
nodes = []
for t in nodeTypes:
    n = NodegraphAPI.CreateNode(t,rootNode)
    nodes.append(n)

NodeUtils.WireInlineNodes(rootNode, nodes)