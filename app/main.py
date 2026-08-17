from fastapi import FastAPI

app = FastAPI(
    title="TFM Container Security Lab",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "service": "tfm-container-security",
        "message": "Container security lab is running"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }
