import datetime

# 단일 노드의 현재 값 출력 함수 정의
def get_current_node_value(client):
    # 가져올 노드의 ID를 문자열로 지정
    nodeid = "ns=12;i=29576"
    # nodeid = ns=12;i=UTAGID 
    # nodeid는 location이나 source에 상관없이 위 법칙에 따라서 구성된다.
    # UTAGID는 ctc_tag 테이블에서 조회
    node = client.get_node(nodeid)    
    print(f"node: {node}, Value: {node.get_value()}, Timestamp : {datetime.datetime.now()}")

# 다수 노드의 현재 값 출력 함수 정의
def get_current_nodes_values(client):
    node_list = [
        client.get_node("ns=12;i=29576"),
        client.get_node("ns=12;i=29577"),
        client.get_node("ns=12;i=29578"),
    ]
    values = client.get_values(node_list)
    for i, value in enumerate(values):
        print(f"node: {node_list[i]}, Value: {value}, Timestamp : {datetime.datetime.now()}")

# 단일 노드의 과거 값(History) 출력 함수 정의
def get_histroy_node_value(client):
    end_time = datetime.datetime.now()
    start_time = end_time - datetime.timedelta(hours=1)
    # 선택한 시간 범위에서 노드의 과거 데이터를 가져온다
    # 주어진 시간에 값이 없으면, 마지막으로 기록된 값을 가져온다
    node = client.get_node(nodeid="ns=12;i=29576")    
    response = node.read_raw_history(start_time, end_time, 3600) 
    for result in response:
        print(f"node: {node}, Value: {result.Value.Value} Timestamp: {result.SourceTimestamp}")


def get_history_nodes_values(client):
    # 또는 여러 개의 노드를 한 번에 읽을 수도 있습니다.
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
