from opcua import Client
import datetime

# OPC UA ������ ����
client = Client("opc.tcp://000.000.000.000:51235")

# ����
client.connect()

# ns=12;i=UTAGID 
# NodeId�� location�̳� source�� ������� �� ��Ģ�� ���� ����.
# UTAGID�� ctc_tag ���̺��� ��ȸ

# ������ ����� ID�� ���ڿ��� ����
nodeId = "ns=12;i=29576" 
node = client.get_node(nodeId) 

# ����� ���� �� ���
print(f"Value: {node.get_value()} Timestamp : {datetime.datetime.now()}");

# ��� ���� �� ���
end_time = datetime.datetime.now()
start_time = end_time - datetime.timedelta(hours=1)

# ������ �ð� �������� ����� ���� �����͸� �����´�
# �־��� �ð��� ���� ������, ���������� ��ϵ� ���� �����´�
response  = node.read_raw_history(start_time, end_time, 3600) 

for result in response:
      print(f"Value: {result.Value.Value} Timestamp: {result.SourceTimestamp}")

# OPC UA ���� ���� ����
client.disconnect()

# namespace ��� ���
#helper.browse_namespace(client)

# ��Ʈ ������ ��� ��� Ž��
#root = client.get_root_node()
#helper.browse_node(root)




    