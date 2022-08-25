from wifi_lib import conecta
from umqtt.simple import MQTTClient
import time

wifi_ssid = 'SEU-SSID-WIFI'
wifi_password = 'SUA-SENHA'

User_ID = 'mwa0000018404630'
MQTT_API_Key = '233I6LSDM9ND8RHW'
mqtt_client_id = '78b4fb22af3348afa55f28a39be10b37' # Um valor aleatório com 32 caracteres (https://keygen.io/ usar "Laravel Encryption Key")
Write_API_Key = 'TMME9A59C8PN4QFB'
Read_API_Key = 'YC6F436J9OEFZY07'
Channel_ID = '1055609'

mqtt_server = 'mqtt.thingspeak.com'
mqtt_port = 1883

        
print("Conectando...")
station = conecta(wifi_ssid, wifi_password)
if not station.isconnected():
    print("Nao conectado!...")
else:
    print("Conectado!...")
    client = MQTTClient(mqtt_client_id, mqtt_server, mqtt_port, User_ID, MQTT_API_Key)
    client.connect()
    for i in range(0, 5):
        # publica com a primeira string no formato "channels/<channelID>/publish/<apikey>"
        # publica com a segunda string no formato "field1=valor&field2=<valor>"
        client.publish('channels/{}/publish/{}'.format(Channel_ID, Write_API_Key),'field1={}&field2={}'.format(i,5-i))
        time.sleep(15)

    client.disconnect()
    time.sleep(1)
    station.disconnect()


