from opcua import Client
import opchelper as helper 

# OPC UA ������ ����
client = Client("opc.tcp://000.000.000.000:51235")

# ����
client.connect()

# ���� ����� ���� �� ���
helper.get_current_node_value(client)

# �ټ� ����� ���� �� ���
helper.get_current_nodes_values(client)

# ���� ����� ���� ��(History) ���
helper.get_histroy_node_value(client)

# �ټ� ����� ���� ��(Histroy) ���
helper.get_history_nodes_values(client)

# OPC UA ���� ���� ����
client.disconnect()