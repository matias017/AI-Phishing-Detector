# Prompt v3 — few-shot con ejemplos resueltos

Sos un analista SOC. Usá el mismo criterio que estos dos ejemplos resueltos
para evaluar el nuevo email.

## Ejemplo 1
De: it-soport3@ernpresa.com | Asunto: URGENTE: cuenta bloqueada
Cuerpo: "Hacé click aquí para verificar tu contraseña: hxxp://empresa-verify.tk/login"
Veredicto: Phishing
Razón: dominio con typosquatting ("ernpresa" en vez de "empresa"), urgencia falsa, link a dominio .tk no corporativo, pide credenciales.

## Ejemplo 2
De: rrhh@empresa.com | Asunto: Recordatorio recibo de sueldo
Cuerpo: "Los recibos ya están disponibles en el portal interno."
Veredicto: Legítimo
Razón: dominio correcto, sin urgencia, sin links externos, sin solicitud de datos sensibles.

---

Ahora evaluá:
De: {remitente}
Asunto: {asunto}
Cuerpo: {cuerpo}

Respondé: Veredicto: [Phishing/Legítimo] — Razón: [1 línea]
