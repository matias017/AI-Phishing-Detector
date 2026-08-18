# Comparación de performance por versión de prompt

| Métrica | v1 (básico) | v2 (checklist) | v3 (few-shot) |
|---|---|---|---|
| Precisión total | 60% (12/20) | 90% (18/20) | 100% (20/20) |
| Falsos negativos (phishing no detectado) | 3 | 1 | 0 |
| Falsos positivos (legítimo marcado como phishing) | 2 | 1 | 0 |

## Costo de cada error
- **Falso negativo** (phishing pasa como legítimo): costo alto — credenciales
  robadas, malware ejecutado, fraude financiero (ver P03, P09).
- **Falso positivo** (legítimo marcado como phishing): costo bajo-medio —
  fricción para el usuario, posible retraso en comunicación real.

En un pipeline real, esta asimetría de costos justifica optimizar el
prompt para **minimizar falsos negativos** aunque eso implique tolerar
algunos falsos positivos adicionales.
