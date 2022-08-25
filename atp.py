#Nome: Marcos Alarcon

#Importação das Classes utilizadas
import dht
import machine
import time
from wifi_lib import conecta
from umqtt.simple import MQTTClient

#Carrega as variáveis dos sensores
d = dht.DHT11(machine.Pin(4))
r = machine.Pin(2, machine.Pin.OUT)

#Carrega as variáveis para conexão com a internet
wifi_ssid = 'VIVOFIBRA-5910_CONVIDADO'
wifi_senha = 'EBENEZER'

#Carrega as variáveis do Thingspeak para autenticação e envio
User_ID = 'mwa0000024002702'                        # Meu código de identificação de usuário na Thingspeak
MQTT_API_Key = 'CAWNXE511DYE8ERN'                   # Chave de Usuário da API na Thingspeak
mqtt_client_id = 'Vvac57TVRq5Zf9BnBeTJjwzCE6Y8Uvb7' # Um valor aleatório com 32 caracteres (https://keygen.io/ usado o "Laravel Encryption Key")
Write_API_Key = '5U6BIXBWE56E3TZE'                  # Chave da API de escrita do Thingspeak
Read_API_Key = 'FXX19ONBPJS8SIBO'                   # Chave da API de leitura do Thingspeak
Channel_ID = '1515032'                              # Código de identificação do meu canal no Thingspeak

mqtt_server = 'mqtt.thingspeak.com'                 # Link do servidor de envio do Thingspeak
mqtt_port = 1883                                    # porta de comunicação do servidor de envio do Thingspeak

while True:
    d.measure() #afere a temperatura e a umidade
    print("Temperatura = {}     Umidade = {}".format(d.temperature(), d.humidity())) 
    if d.temperature() > 31 or d.humidity() > 70:  #Se a temperatura for maior que 31 graus ou a umidade maior que 70%, será acionado o relê que liga a refrigeração 

        if r.value() == 0:  #Se o relê estava desligado
          print("\nMuito quente, a refrigeração foi ligada!\n")

        r.value(1) # Liga o relê
        
    else:
        if r.value() == 1:  #Se o relê estava ligado
          print("\nRefrescou um pouco, a refrigeração foi desligada!\n")

        r.value(0) # Desliga o relê

        
    print("Conectando...")
    station = conecta(wifi_ssid, wifi_senha) #Verifica a conexão com a internet

    if not station.isconnected():
        print("Não conectado!...")
    else:
        print("Conectado!...")

        # Conexão com o servidor Thingspeak
        client = MQTTClient(mqtt_client_id, mqtt_server, mqtt_port, User_ID, MQTT_API_Key)
        client.connect()
        # Após conectar, publica os 3 campos medidos (temperatura, umidade e o status do relê, se está ligada a refrigeração ou não)
        client.publish('channels/{}/publish/{}'.format(Channel_ID, Write_API_Key),'field1={}&field2={}&field3={}'.format(d.temperature(),d.humidity(),r.value()))
        
        time.sleep(15)          #Aguarda 15 segundos devido a limitação da conta gratuíta do Thingspeak
        client.disconnect()     #Desconecta do Thingspeak
        time.sleep(1)           #Aguarda 1 segundo para finalizar a conexão com a Thingspeak
        station.disconnect()    #Desconecta da Internet


