import socket

def test_emergency_port(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"✅ [SUCESSO]: PORTA {port} ABERTA PARA EMERGÊNCIA")
        else:
            print(f"❌ [BLOQUEIO]: PORTA {port} FECHADA (ERRO {result})")
        s.close()
    except Exception as e:
        print(f"⚠️ [FALHA]: ERRO NA PORTA {port}: {e}")

print("\n--- MOTOR D3 ESPRIT: BUSCANDO BRECHA DE REDE ---")
# Testando portas comuns que costumam ficar abertas em redes restritas
alvos = [53, 80, 443, 8080, 1194]
for p in alvos:
    test_emergency_port("8.8.8.8", p)

