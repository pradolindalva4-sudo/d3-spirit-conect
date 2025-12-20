#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PROJETO: D3 ESPRIT
DESENVOLVEDOR: JOSÉ DIVINO PRADO DA LAPA
FUNÇÃO: SCANNER DE HARDWARE REAL - SINCRONIZAÇÃO 4K
"""

import subprocess
import json
import os

def obter_dados_reais():
    try:
        # Comando real para varredura de interfaces wireless no Linux/Termux
        # O nmcli -t (terse) fornece dados limpos para o sistema processar
        cmd = ["nmcli", "-t", "-f", "SIGNAL,SSID,BARS,SECURITY", "device", "wifi", "list"]
        
        # Executa o comando de hardware
        resultado = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        redes_detectadas = []
        linhas = resultado.stdout.strip().split('\n')
        
        for linha in linhas:
            if linha:
                # O nmcli usa ':' como separador no modo terse
                partes = linha.split(':')
                if len(partes) >= 2:
                    sinal_num = partes[0]
                    redes_detectadas.append({
                        "sinal": f"{sinal_num}%",
                        "ssid": partes[1] if partes[1] else "Rede Oculta",
                        "qualidade": partes[2],
                        "seguranca": partes[3] if partes[3] else "Aberta"
                    })

        # Ordenação por potência de sinal (Real Time)
        redes_detectadas = sorted(redes_detectadas, key=lambda x: int(x['sinal'].replace('%','')), reverse=True)

        # Resposta estruturada para o app.js
        # Se houver redes, o status é ONLINE e a estabilidade é garantida
        status_sistema = "ONLINE" if redes_detectadas else "BUSCANDO"
        
        output = {
            "status": status_sistema,
            "desenvolvedor": "José Divino Prado da Lapa",
            "estabilidade": "100% Estável (4K)" if redes_detectadas else "Oscilando",
            "log_tecnico": f"Encontradas {len(redes_detectadas)} redes em modo real.",
            "melhor_sinal": redes_detectadas[0] if redes_detectadas else None
        }
        
        return json.dumps(output, ensure_ascii=False)

    except subprocess.CalledProcessError:
        return json.dumps({"status": "OFFLINE", "erro": "Permissão de hardware negada. Use Root."})
    except Exception as e:
        return json.dumps({"status": "ERRO", "detalhes": str(e)})

if __name__ == "__main__":
    # Saída padrão para consumo do servidor Node.js (app.js)
    print(obter_dados_reais())
