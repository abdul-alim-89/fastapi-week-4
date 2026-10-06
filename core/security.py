import jwt
from pwdlib import PasswordHash
from datetime import datetime, date, timedelta, timezone

SECREAT_KEY = "0fW=Kl+1l*hQa-W<"
ALGORITHM = "HS256"
EXPIRY_TIME_IN_MINUTES = 15

password_hash = PasswordHash.recommended()

def hash_password(pswd: str) -> str:
    return password_hash.hash(pswd)

def verify_hash_password(pswd: str, hpswd: str) -> bool:

    return password_hash.verify(pswd, hpswd)

print(hash_password("abdulalim"))
# print(verify_hash_password("abdulalim", ""))

def generate_token(userid: int):

    exp = datetime.now(timezone.utc) + timedelta(minutes=EXPIRY_TIME_IN_MINUTES)

    payload = {"sub": str(userid), "exp": exp}

    return jwt.encode(payload, SECREAT_KEY, ALGORITHM)

def decode_token(token: str):
    payload = jwt.decode(token, SECREAT_KEY, ALGORITHM)
    return payload


print(generate_token(52))
