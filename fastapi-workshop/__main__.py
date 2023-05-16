import uvicorn

from setings import settings


#При обновлении кода сервер будет перезагружаться автоматически 
uvicorn.run (
    "workshop.app:app",
    host = settings.server_host,
    port = settings.server_port,
    reload=True,
)
if __name__ == '__main__':
    from multiprocessing import freeze_support
    freeze_support()
    # Ваш код здесь