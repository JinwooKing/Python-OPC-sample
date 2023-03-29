# -*- coding: utf-8 -*-
import datetime

# ���� ����� ���� �� ��� �Լ� ����
def get_current_node_value(client, nodeid):
    # ������ ����� ID�� ���ڿ��� ����
    node = client.get_node(nodeid)    
    #print(f"node: {node}, Value: {node.get_value()}, Timestamp : {datetime.datetime.now()}")
    rtnVal = f"node: {node}, Value: {node.get_value()}, Timestamp : {datetime.datetime.now()}"
    return rtnVal
    

# �ټ� ����� ���� �� ��� �Լ� ����
def get_current_nodes_values(client, node_list):
    rtnVal = ""
    #node_list = [
    #    client.get_node("ns=12;i=29576"),
    #    client.get_node("ns=12;i=29577"),
    #    client.get_node("ns=12;i=29578"),
    #]
    node_list = list(map(client.get_node, node_list))
    values = client.get_values(node_list)
    for i, value in enumerate(values):
        #print(f"node: {node_list[i]}, Value: {value}, Timestamp : {datetime.datetime.now()}")
        rtnVal += f"node: {node_list[i]}, Value: {value}, Timestamp : {datetime.datetime.now()} \n"
    return rtnVal

# ���� ����� ���� ��(History) ��� �Լ� ����
def get_histroy_node_value(client, nodeid, stdt, enddt):
    rtnVal = ""
    #end_time = datetime.datetime.now()
    #start_time = end_time - datetime.timedelta(hours=1)
    end_time = enddt
    start_time = stdt
    #nodeid="ns=12;i=29576"
    # ������ �ð� �������� ����� ���� �����͸� �����´�
    # �־��� �ð��� ���� ������, ���������� ��ϵ� ���� �����´�
    node = client.get_node(nodeid)    
    response = node.read_raw_history(start_time, end_time, 3600) 
    for result in response:
        #print(f"node: {node}, Value: {result.Value.Value} Timestamp: {result.SourceTimestamp}")
        rtnVal += f"node: {node}, Value: {result.Value.Value} Timestamp: {result.SourceTimestamp} \n"
    return rtnVal

# �ټ� ����� ���� ��(Histroy) ���
def get_history_nodes_values(client, node_list, stdt, enddt):
    rtnVal = ""
    #end_time = datetime.datetime.now()
    #start_time = end_time - datetime.timedelta(hours=1)
    end_time = enddt
    start_time = stdt
    node_list = list(map(client.get_node, node_list))
    for node in node_list:
        response = node.read_raw_history(start_time, end_time, 3600)
        for result in response:
            #print(f"node: {node}, Value: {result.Value.Value} Timestamp: {result.SourceTimestamp}")
            rtnVal += f"node: {node}, Value: {result.Value.Value} Timestamp: {result.SourceTimestamp} \n"
    return rtnVal

