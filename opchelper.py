# -*- coding: utf-8 -*-
import datetime

# 단일 노드의 현재 값 출력 함수 정의
def get_current_node_value(client, nodeid):
    # 가져올 노드의 ID를 문자열로 지정
    node = client.get_node(nodeid)    
    #print(f"node: {node}, Value: {node.get_value()}, Timestamp : {datetime.datetime.now()}")
    rtnVal = f"node: {node}, Value: {node.get_value()}, Timestamp : {datetime.datetime.now()}"
    return rtnVal
    

# 다수 노드의 현재 값 출력 함수 정의
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

# 단일 노드의 과거 값(History) 출력 함수 정의
def get_histroy_node_value(client, nodeid, stdt, enddt):
    rtnVal = ""
    #end_time = datetime.datetime.now()
    #start_time = end_time - datetime.timedelta(hours=1)
    end_time = enddt
    start_time = stdt
    #nodeid="ns=12;i=29576"
    # 선택한 시간 범위에서 노드의 과거 데이터를 가져온다
    # 주어진 시간에 값이 없으면, 마지막으로 기록된 값을 가져온다
    node = client.get_node(nodeid)    
    response = node.read_raw_history(start_time, end_time, 3600) 
    for result in response:
        #print(f"node: {node}, Value: {result.Value.Value} Timestamp: {result.SourceTimestamp}")
        rtnVal += f"node: {node}, Value: {result.Value.Value} Timestamp: {result.SourceTimestamp} \n"
    return rtnVal

# 다수 노드의 과거 값(Histroy) 출력
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

