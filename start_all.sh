cat << 'EOF' > start_all.sh
#!/bin/bash
echo "🚀 [D3 ESPRIT]: INICIALIZANDO ENGENHARIA JOSÉ DIVINO..."

# 1. Limpeza de Segurança
./clean.sh 

# 2. Ativação do Motor de Injeção (7 bytes) em segundo plano
python d3_emergency.py & 

# 3. Inicialização do Monitor de Buffer (90GB)
python monitor.py & 

# 4. Ativação do Painel Visual Colorido
node app.js
EOF

chmod +x start_all.sh
