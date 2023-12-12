from fastapi import APIRouter, status

from ..schemas.activities import Activity

router = APIRouter(prefix='/activities', tags=['Activities'])

@router.post('',name='Create New Activity', status_code=status.HTTP_201_CREATED)
def new_activity(payload: Activity) -> Activity:
  return payload