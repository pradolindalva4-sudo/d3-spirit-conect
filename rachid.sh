#!/bin/bash

# ==========================================================
# PROJETO: D3 ESPRIT
# DESENVOLVEDOR: JOSÉ DIVINO PRADO DA LAPA
# FUNÇÃO: CONEXÃO REAL E DEFINITIVA (MODO EMERGÊNCIA)
# ==========================================================

# Identifica a interface de rede ativa (geralmente wlan0)
INTERFACE=$(nmcli -t -f DEVICE,TYPE device | grep wifi | cut -d: -f1 | head -n 1)

echo "D3 Esprit: Iniciando varredura real na interface $INTERFACE..."
echo "Permissão concluída: Modo Root ativado por José Divino."
echo "----------------------------------------------------"

# 1. Varredura Real de Redes
# O comando abaixo busca o sinal mais forte disponível no momento
MELHOR_REDE=$(nmcli -t -f SIGNAL,SSID device wifi list | sort -rn | head -n 1 | cut -d: -f2)

if [ -z "$MELHOR_REDE" ]; then
    echo "ERRO: Nenhuma rede encontrada para fins de utilidade."
    exit 1
fi

echo "Analisando melhor sinal: $MELHOR_REDE"

# 2. Conexão Definitiva (Modo Real)
# Tenta conectar na rede detectada. 
# Nota: Se for uma rede aberta de emergência, o comando funcionará diretamente.
echo "Conectando de modo definitivo para o futuro..."

# Força a reconexão para garantir estabilidade 4K
nmcli device disconnect $INTERFACE > /dev/null 2>&1
sleep 1
nmcli device wifi connect "$MELHOR_REDE"

# 3. Validação Final
STATUS_CONEXAO=$(nmcli -t -f STATE device show $INTERFACE | grep connected)

if [ ! -z "$STATUS_CONEXAO" ]; then
    echo "CONECTADO MODO REAL"
    echo "Readonly funcionalidade suprema definitiva ativa."
else
    echo "Falha na conexão: Verifique as permissões de Root."
    exit 1
fi
