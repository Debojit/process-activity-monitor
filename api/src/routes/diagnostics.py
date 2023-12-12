from fastapi import APIRouter, status
from fastapi.responses import PlainTextResponse

router = APIRouter(prefix='/diagnostics', tags=['Diagnostics'])

@router.get('/ping', status_code=status.HTTP_200_OK, response_class=PlainTextResponse)
def ping() -> None:
  return 'OK'