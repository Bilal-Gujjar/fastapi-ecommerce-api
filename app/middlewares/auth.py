from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from jose import jwt, JWTError
from app.core.config import settings

app = FastAPI()

@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    if request.url.path not in ["/api/v1/login", "/api/v1/signup", "/"]:
        authorization: str = request.headers.get("Authorization")
        if not authorization:
            return JSONResponse(status_code=401, content={"message": "Not authenticated"})
        scheme, param = authorization.split()
        if scheme.lower() != 'bearer':
            return JSONResponse(status_code=401, content={"message": "Invalid authentication scheme"})
        try:
            payload = jwt.decode(param, settings.secret_key, algorithms=[settings.algorithm])
            request.state.user = payload.get("sub")  # Attach user information to the request state
        except JWTError as e:
            # Instead of raising an exception, return a JSON response with the error details
            return JSONResponse(status_code=401, content={"message": "Could not validate token"})
    return await call_next(request)

# ... other parts of your FastAPI app
