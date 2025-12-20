#!/bin/bash
echo "🧹 [LIMPEZA]: Liberando a porta 8080 e resetando processos..."
fuser -k 8080/tcp 2>/dev/null
pkill node
pkill python
echo "✅ [STATUS]: Ambiente limpo. Pronto para decolar!"
