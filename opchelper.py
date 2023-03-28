# ��� ��� ��� �Լ� ����
def browse_namespace(client):
    for i, namespace in enumerate(client.get_namespace_array()):
        print(f"namespace[{i}]: {namespace}")

# ��� Ž�� �Լ� ����
def browse_node(root):
    for i, child_node in enumerate(root.get_children()):
        print(f"child_node[{i}]: {child_node}")
        browse_node(child_node)