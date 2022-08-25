from wifi_lib import conecta
import urequests

print("Conectando...")
station = conecta("VIVOFIBRA-5910_CONVIDADO", "EBENEZER")
if not station.isconnected():
    print("Não conectado!")
else:
    print("Conectado!!!")
    print("Acessando o site...")
    resposta = urequests.get("http://teste.afonsomiguel.com")
    print("Página acessada:")
    print(resposta.text)
    station.disconnect()