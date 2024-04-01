import uvicorn
from fastapi import FastAPI

async def start_event():
    await write_log(msg='System login')

async def shutdown_event():
    await write_log(msg='System logout')

app = FastAPI(title="PYTHON_VERSION",
        description="Harbor docker image",
        version="1.0.0",
        on_startup=[start_event],
        on_shutdown=[shutdown_event])


if __name__ == '__main__':
    uvicorn.run(
        app='main:app',
        host='0.0.0.0',
        port=8093,
        debug=False,
        reload=True,)