# Lecciones aprendidas

1. **El prompt básico es insuficiente para producción.** Sin criterios
   explícitos, el modelo confunde patrones superficiales (links, urgencia
   comercial) con intención maliciosa real — 40% de error en v1.

2. **Descomponer el criterio en una checklist mejora mucho la precisión**
   (60% → 90%). Forzar al modelo a razonar paso a paso (dominio, urgencia,
   links, solicitud sensible, ortografía) antes de concluir reduce errores
   de "juicio apurado".

3. **Los ejemplos few-shot ayudan a calibrar casos límite** (P07, el
   dominio con país distinto). Un solo ejemplo bien elegido puede corregir
   un patrón de error sistemático.

4. **El dataset es chico (20 casos) — 100% de precisión en v3 no significa
   que el prompt sea perfecto**, significa que funciona bien para estos
   patrones específicos. En producción haría falta un dataset más grande
   y variado (nuevas técnicas de phishing, otros idiomas, etc.) para
   validar de verdad.

5. **Conclusión operativa:** un LLM bien afinado con checklist + few-shot
   puede automatizar un primer filtro efectivo de phishing, priorizando
   minimizar falsos negativos por el costo asimétrico del error. Pero
   sigue necesitando monitoreo continuo y revisión humana de los casos
   de baja confianza.
