from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from router import master_router
from cfg import *

def create_fastapi() -> FastAPI:
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=False,
        allow_methods=['*']
    )
    app.include_router(master_router)

    return app

app = create_fastapi()

if __name__ == '__main__':
    uvicorn.run(**run_cfg)
