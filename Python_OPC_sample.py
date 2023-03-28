from opcua import Client
import datetime

# OPC UA 서버에 연결
client = Client("opc.tcp://000.000.000.000:51235")

# 연결
client.connect()

# ns=12;i=UTAGID 
# NodeId는 location이나 source에 상관없이 위 법칙에 따라서 구성.
# UTAGID는 ctc_tag 테이블에서 조회

# 가져올 노드의 ID를 문자열로 지정
nodeId = "ns=12;i=29576" 
node = client.get_node(nodeId) 

# 노드의 현재 값 출력
print(f"Value: {node.get_value()} Timestamp : {datetime.datetime.now()}");

# 노드 과거 값 출력
end_time = datetime.datetime.now()
start_time = end_time - datetime.timedelta(hours=1)

# 선택한 시간 범위에서 노드의 과거 데이터를 가져온다
# 주어진 시간에 값이 없으면, 마지막으로 기록된 값을 가져온다
response  = node.read_raw_history(start_time, end_time, 3600) 

for result in response:
      print(f"Value: {result.Value.Value} Timestamp: {result.SourceTimestamp}")

# OPC UA 서버 연결 종료
client.disconnect()

# namespace 목록 출력
#helper.browse_namespace(client)

# 루트 노드부터 모든 노드 탐색
#root = client.get_root_node()
#helper.browse_node(root)




    