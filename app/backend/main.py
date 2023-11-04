from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

def create_fastapi() -> FastAPI:
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=False,
        allow_methods=['*']
    )

    from router import master_router
    app.include_router(master_router)

    return app


app = create_fastapi()

from cfg import *
if __name__ == '__main__':
    uvicorn.run(**run_cfg)
