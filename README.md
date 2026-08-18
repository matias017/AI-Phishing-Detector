# AI# AI-Phishing-Detector

Evaluación de un LLM como clasificador de phishing, comparando tres
versiones de prompt (básico, checklist, few-shot) contra un dataset
sintético de 20 emails (10 legítimos, 10 phishing).

## Nota
Dataset sintético, creado para este ejercicio educativo — no proviene
de correos reales de ninguna organización.

## Resultado
- Prompt v1 (básico): 60% de precisión
- Prompt v2 (checklist): 90% de precisión
- Prompt v3 (few-shot): 100% de precisión (sobre este dataset acotado)

## Conclusión
Descomponer el criterio de análisis y dar ejemplos resueltos mejora
sustancialmente la performance del modelo. El diseño del prompt debe
priorizar minimizar falsos negativos, dado el costo asimétrico de un
phishing no detectado frente a un falso positivo.-Phishing-Detector
