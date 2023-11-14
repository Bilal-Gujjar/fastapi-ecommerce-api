from fastapi import Request, HTTPException
from jose import jwt
from app.core.config import settings

async def auth_middleware(request: Request, call_next):
    if request.url.path not in ["/api/v1/login", "/api/v1/signup", "/" ,"/docs"]:
        authorization: str = request.headers.get("Authorization")
        if not authorization:
            raise HTTPException(status_code=401, detail="Not authenticated")
        scheme, param = authorization.split()
        if scheme.lower() != 'bearer':
            raise HTTPException(status_code=401, detail="Invalid authentication scheme")
        try:
            payload = jwt.decode(param, settings.secret_key, algorithms=[settings.algorithm])
            request.state.user = payload.get("sub")  # You can attach user information to the request state
        except jwt.JWTError as e:
            raise HTTPException(status_code=401, detail="Could not validate credentials") from e
    return await call_next(request)
