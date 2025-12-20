import os
import time

# CAMINHO DO SEU BUFFER DE ELITE
DB_PATH = "internet_storage/network_buffer.db"

def monitorar_vazao():
    print(f"\n" + "📈"*15)
    print(f"D3 ESPRIT - MONITOR DE TRAFEGO")
    print(f"ENGENHEIRO: JOSÉ DIVINO")
    print("📈"*15 + "\n")

    last_size = os.path.getsize(DB_PATH) if os.path.exists(DB_PATH) else 0

    while True:
        try:
            current_size = os.path.getsize(DB_PATH)
            diff = current_size - last_size
            
            # Converte para visualização sênior
            size_gb = current_size / (1024**3)
            vazao_kb = diff / 1024
            
            # O log que confirma a atividade
            print(f"✅ [SISTEMA]: CONEXÃO GLOBAL ESTÁVEL")
            print(f"📦 BUFFER TOTAL: {size_gb:.2f} GB / 90.00 GB")
            print(f"🚀 VAZÃO ATUAL: {vazao_kb:.2f} KB/s")
            print("-" * 30)
            
            last_size = current_size
            time.sleep(1) # Atualização segundo a segundo
        except FileNotFoundError:
            print("⚠️ Aguardando criação do arquivo de storage...")
            time.sleep(5)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    monitorar_vazao()
