import threading
from fastapi import FastAPI
import uvicorn

from tautulli.webhook import router as tautulli_router
from ui.routes import router as ui_router
from scheduler import scheduler_loop

app = FastAPI()
app.include_router(tautulli_router)
app.include_router(ui_router)

threading.Thread(target=scheduler_loop, daemon=True).start()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8787)
