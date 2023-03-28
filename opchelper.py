import datetime

# ���� ����� ���� �� ��� �Լ� ����
def get_current_node_value(client):
    # ������ ����� ID�� ���ڿ��� ����
    nodeid = "ns=12;i=29576"
    # nodeid = ns=12;i=UTAGID 
    # nodeid�� location�̳� source�� ������� �� ��Ģ�� ���� �����ȴ�.
    # UTAGID�� ctc_tag ���̺��� ��ȸ
    node = client.get_node(nodeid)    
    print(f"node: {node}, Value: {node.get_value()}, Timestamp : {datetime.datetime.now()}")

# �ټ� ����� ���� �� ��� �Լ� ����
def get_current_nodes_values(client):
    node_list = [
        client.get_node("ns=12;i=29576"),
        client.get_node("ns=12;i=29577"),
        client.get_node("ns=12;i=29578"),
    ]
    values = client.get_values(node_list)
    for i, value in enumerate(values):
        print(f"node: {node_list[i]}, Value: {value}, Timestamp : {datetime.datetime.now()}")

# ���� ����� ���� ��(History) ��� �Լ� ����
def get_histroy_node_value(client):
    end_time = datetime.datetime.now()
    start_time = end_time - datetime.timedelta(hours=1)
    # ������ �ð� �������� ����� ���� �����͸� �����´�
    # �־��� �ð��� ���� ������, ���������� ��ϵ� ���� �����´�
    node = client.get_node(nodeid="ns=12;i=29576")    
    response = node.read_raw_history(start_time, end_time, 3600) 
    for result in response:
        print(f"node: {node}, Value: {result.Value.Value} Timestamp: {result.SourceTimestamp}")


def get_history_nodes_values(client):
    # �Ǵ� ���� ���� ��带 �� ���� ���� ���� �ֽ��ϴ�.
    end_time = datetime.datetime.now()
    start_time = end_time - datetime.timedelta(hours=1)
    node_list = [
        client.get_node("ns=12;i=29576"),
        client.get_node("ns=12;i=29577"),
        client.get_node("ns=12;i=29578"),
    ]
    for node in node_list:
        response = node.read_raw_history(start_time, end_time, 3600)
        for result in response:
            print(f"node: {node}, Value: {result.Value.Value} Timestamp: {result.SourceTimestamp}")
