#Эндпоинты касающиеся операций
from typing import List
from fastapi import APIRouter
from sqlalchemy.orm import Session
from ..   import tables 
from fastapi import Depends
from database import get_session
from ..models.operations import Operation


#все обработчики будут отчитываться от /opeartions
router = APIRouter(
    prefix='/operations',
)

#Создаем возвращаемое значение 
@router.get('/', response_model=List[Operation])
def get_operations(session:Session = Depends(get_session)):
    return []
