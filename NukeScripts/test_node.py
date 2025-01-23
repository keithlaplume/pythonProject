import nuke


def run_script():
    my_node = nuke.nodes.Read()
    print("Hello world!")


def create_test_node():
    test_node = nuke.createNode("Group")
    test_node.addKnob(nuke.PyScript_Knob("run_script", "Create Read Node"))
    test_node['run_script'].setCommand("run_script()")

toolbar = nuke.toolbar("Nodes")
my_menu = toolbar.addMenu("Custom Tools")
my_menu.addCommand("Create Test Node", create_test_node)
