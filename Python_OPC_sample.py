from opcua import Client
import opchelper as helper 

# OPC UA 서버에 연결
client = Client("opc.tcp://000.000.000.000:51235")

# 연결
client.connect()

# 단일 노드의 현재 값 출력
helper.get_current_node_value(client)

# 다수 노드의 현재 값 출력
helper.get_current_nodes_values(client)

# 단일 노드의 과거 값(History) 출력
helper.get_histroy_node_value(client)

# 다수 노드의 과거 값(Histroy) 출력
helper.get_history_nodes_values(client)

# OPC UA 서버 연결 종료
client.disconnect()