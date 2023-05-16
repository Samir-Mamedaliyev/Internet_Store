#Эндпоинты касающиеся операций
from fastapi import APIRouter

#все обработчики будут отчитываться от /opeartions
router = APIRouter(
    prefix='/operations',
)


@router.get('/')
def get_operations():
    return []
