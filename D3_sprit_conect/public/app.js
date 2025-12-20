// CONFIGURAÇÕES JOSÉ DIVINO - D3 ESPRIT
let sistemaAtivo = false;
let bytesInjetados = 0;
const canvas = document.getElementById('liveGraph');
const ctx = canvas.getContext('2d');

// Elementos da Interface Colorida
const speedDisplay = document.getElementById('speed-val');
const bufferDisplay = document.getElementById('buffer-val');
const powerBtn = document.getElementById('power-btn');
const logStream = document.getElementById('log-stream');
const connStatus = document.getElementById('conn-status');

// 1. Simulação de Dados Reais baseada no terminal
function atualizarDados() {
    if (sistemaAtivo) {
        // Simula a recepção dos 7 bytes injetados
        let vazoAtual = (Math.random() * 15.5 + 7.0).toFixed(2);
        bytesInjetados += 0.00001; // Crescimento do buffer de 90GB
        
        speedDisplay.innerText = vazoAtual;
        bufferDisplay.innerText = bytesInjetados.toFixed(4);
        
        // Log dinâmico na tela
        logStream.innerHTML = `💎 [TÚNEL]: 7 bytes injetados no sistema...<br>${logStream.innerHTML.substring(0, 100)}`;
    }
}

// 2. Função de Ligar/Desligar (Power)
function togglePower() {
    sistemaAtivo = !sistemaAtivo;
    
    if (sistemaAtivo) {
        powerBtn.classList.add('active');
        powerBtn.innerText = "SISTEMA ONLINE";
        connStatus.innerText = "STATUS: CONEXÃO GLOBAL ESTÁVEL"; //
        connStatus.style.color = "#00f2ff";
        console.log("🚀 D3 ESPRIT: Inicializando Gateway 443");
    } else {
        powerBtn.classList.remove('active');
        powerBtn.innerText = "LIGAR PROJETO";
        connStatus.innerText = "STATUS: STANDBY";
        connStatus.style.color = "#444";
    }
}

// 3. Gráfico de Ondas Dinâmico
function drawGraph() {
    canvas.width = canvas.offsetWidth;
    canvas.height = canvas.offsetHeight;
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    ctx.beginPath();
    ctx.lineWidth = 2;
    ctx.strokeStyle = sistemaAtivo ? '#00f2ff' : '#222';
    
    for (let i = 0; i < canvas.width; i++) {
        const amplitude = sistemaAtivo ? 30 : 5;
        const freq = 0.02;
        const y = (canvas.height / 2) + Math.sin(i * freq + Date.now() * 0.01) * amplitude;
        if (i === 0) ctx.moveTo(i, y);
        else ctx.lineTo(i, y);
    }
    ctx.stroke();
    requestAnimationFrame(drawGraph);
}

// Inicialização
setInterval(atualizarDados, 1000);
drawGraph();
