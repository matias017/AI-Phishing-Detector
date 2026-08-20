
import os
import csv
import json
import time
import google.generativeai as genai

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-2.0-flash")

DATASET = [
    {"id": "E01", "real": "Legitimo", "remitente": "rrhh@empresa.com", "asunto": "Recordatorio: entrega de recibo de sueldo", "cuerpo": "Hola equipo, les recordamos que los recibos ya están disponibles en el portal interno."},
    {"id": "E02", "real": "Legitimo", "remitente": "it-soporte@empresa.com", "asunto": "Mantenimiento programado del servidor", "cuerpo": "El viernes 21/08 de 22:00 a 23:00 habrá mantenimiento. Los sistemas podrían no estar disponibles."},
    {"id": "E03", "real": "Legitimo", "remitente": "notificaciones@mercadolibre.com.ar", "asunto": "Tu producto fue enviado", "cuerpo": "Tu pedido #45892 fue despachado y llegará en 3-5 días hábiles."},
    {"id": "E04", "real": "Legitimo", "remitente": "juan.perez@empresa.com", "asunto": "Reunión de equipo reprogramada", "cuerpo": "Chicos, la reunión de mañana pasa para las 15hs por un conflicto de agenda."},
    {"id": "E05", "real": "Legitimo", "remitente": "facturacion@proveedor-habitual.com", "asunto": "Factura numero 2024-3312", "cuerpo": "Adjuntamos la factura correspondiente al mes de julio. Cualquier consulta, contactarnos."},
    {"id": "E06", "real": "Legitimo", "remitente": "no-reply@linkedin.com", "asunto": "Tenes 3 notificaciones nuevas", "cuerpo": "Alguien vio tu perfil recientemente. Ingresá para ver quién."},
    {"id": "E07", "real": "Legitimo", "remitente": "soporte@banco-real.com.ar", "asunto": "Resumen de tarjeta disponible", "cuerpo": "Tu resumen de agosto ya está disponible para consultar en homebanking."},
    {"id": "E08", "real": "Legitimo", "remitente": "administracion@empresa.com", "asunto": "Actualización de política de vacaciones", "cuerpo": "Se actualizó la política de vacaciones, disponible en la intranet."},
    {"id": "E09", "real": "Legitimo", "remitente": "eventos@camara-empresarial.org", "asunto": "Invitación a webinar gratuito", "cuerpo": "Te invitamos al webinar sobre ciberseguridad el próximo martes."},
    {"id": "E10", "real": "Legitimo", "remitente": "soporte-tecnico@empresa.com", "asunto": "Ticket numero 8821 resuelto", "cuerpo": "Tu ticket fue resuelto. Si el problema persiste, respondé este correo."},
    {"id": "P01", "real": "Phishing", "remitente": "it-soport3@ernpresa.com", "asunto": "URGENTE: tu cuenta será bloqueada en 24hs", "cuerpo": "Hacé click aquí para verificar tu contraseña antes de que se suspenda tu acceso: hxxp://empresa-verify.tk/login"},
    {"id": "P02", "real": "Phishing", "remitente": "seguridad@paypal-secure-verify.com", "asunto": "Actividad sospechosa detectada", "cuerpo": "Detectamos un acceso no autorizado. Confirmá tu identidad ingresando tus datos: hxxp://bit.ly/3xR9klm"},
    {"id": "P03", "real": "Phishing", "remitente": "ceo@empresa.com", "asunto": "Necesito un favor urgente", "cuerpo": "Estoy en una reunión, no puedo hablar. Necesito que compres tarjetas de regalo por 500 dolares y me mandes los códigos ya."},
    {"id": "P04", "real": "Phishing", "remitente": "rrhh-empresa@gmail.com", "asunto": "Nuevo formulario de datos bancarios", "cuerpo": "Actualizá tus datos bancarios para el próximo pago de sueldo en este link: hxxp://empresa-payroll.info/update"},
    {"id": "P05", "real": "Phishing", "remitente": "no-reply@microsft-support.com", "asunto": "Tu licencia de Office expiró", "cuerpo": "Renová tu licencia ahora o perderás acceso a tus documentos: hxxp://ms-office-renew.xyz"},
    {"id": "P06", "real": "Phishing", "remitente": "envios@correo-argentino-tracking.net", "asunto": "Paquete retenido en aduana", "cuerpo": "Tu paquete fue retenido. Pagá la tasa aduanera aquí: hxxp://correoarg-pago.click"},
    {"id": "P07", "real": "Phishing", "remitente": "soporte@empresa.com.co", "asunto": "Actualización obligatoria de contraseña", "cuerpo": "Por seguridad, actualizá tu contraseña ahora mismo: hxxp://empresa-idportal.net"},
    {"id": "P08", "real": "Phishing", "remitente": "admin@empresa-intranet-login.com", "asunto": "Acceso a intranet restringido", "cuerpo": "Tu acceso fue restringido por inactividad. Reactivalo aquí: hxxp://empresa-intranet-login.com/auth"},
    {"id": "P09", "real": "Phishing", "remitente": "finanzas@empresa.com", "asunto": "Comprobante de transferencia adjunto", "cuerpo": "Adjunto comprobante, revisar y confirmar recepción. (adjunto: comprobante_transferencia.exe)"},
    {"id": "P10", "real": "Phishing", "remitente": "soporte-office365@outlook-verify.com", "asunto": "Tu buzón está casi lleno", "cuerpo": "Tu buzón alcanzó el 95% de capacidad. Ampliá el espacio aquí: hxxp://o365-storage-upgrade.info"},
]

PROMPTS = {
    "v1": open("prompts/v1-basico.txt", encoding="utf-8").read(),
    "v2": open("prompts/v2-con-criterios.txt", encoding="utf-8").read(),
    "v3": open("prompts/v3-few-shot.txt", encoding="utf-8").read(),
}


def clasificar(prompt_template, caso):
    prompt = prompt_template.format(remitente=caso["remitente"], asunto=caso["asunto"], cuerpo=caso["cuerpo"])
    resp = model.generate_content(prompt)
    return resp.text.strip()


def extraer_veredicto(texto_crudo):
    t = texto_crudo.lower()
    if "phishing" in t or t.strip() == "si" or t.strip() == "sí":
        return "Phishing"
    return "Legitimo"


def main():
    resultados = []
    for version, prompt_template in PROMPTS.items():
        aciertos = 0
        for caso in DATASET:
            crudo = clasificar(prompt_template, caso)
            veredicto = extraer_veredicto(crudo)
            correcto = veredicto == caso["real"]
            aciertos += correcto
            resultados.append({"prompt_version": version, "id": caso["id"], "real": caso["real"], "veredicto_modelo": veredicto, "correcto": correcto, "respuesta_cruda": crudo})
            time.sleep(4)
        precision = aciertos / len(DATASET) * 100
        print(f"Prompt {version}: {aciertos}/{len(DATASET)} = {precision:.1f}% de precision")

    with open("resultados_reales.json", "w", encoding="utf-8") as f:
        json.dump(resultados, f, ensure_ascii=False, indent=2)

    with open("resultados_reales.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=resultados[0].keys())
        writer.writeheader()
        writer.writerows(resultados)

    print("Guardado: resultados_reales.json y resultados_reales.csv")


if __name__ == "__main__":
    main()
 run_
