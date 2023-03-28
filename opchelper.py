# 노드 목록 출력 함수 정의
def browse_namespace(client):
    for i, namespace in enumerate(client.get_namespace_array()):
        print(f"namespace[{i}]: {namespace}")

# 노드 탐색 함수 정의
def browse_node(root):
    for i, child_node in enumerate(root.get_children()):
        print(f"child_node[{i}]: {child_node}")
        browse_node(child_node)