importScripts('https://storage.googleapis.com/workbox-cdn/releases/7.0.0/workbox-sw.js');

if (workbox) {
  workbox.core.skipWaiting();
  workbox.core.clientsClaim();

  // 1. CAPTURA TOTAL DE TRÁFEGO (Modo Severino)
  // Esta regra intercepta TUDO o que o aparelho tentar acessar
  workbox.routing.registerRoute(
    ({request}) => true, 
    new workbox.strategies.NetworkFirst({
      cacheName: 'd3-full-internet-buffer',
      networkTimeoutSeconds: 5, // Dá tempo para o túnel das portas 53/443 responder
      plugins: [
        new workbox.cacheableResponse.CacheableResponsePlugin({
          statuses: [0, 200],
        }),
        new workbox.expiration.ExpirationPlugin({
          maxEntries: 500,
          maxAgeSeconds: 60 * 60 * 24, // Mantém o cache vivo por 24h
        }),
      ],
    })
  );

  console.log("🚀 Sistema D3: Roteamento de Internet Total Ativado.");
}
