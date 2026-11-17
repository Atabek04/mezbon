from fastapi import FastAPI

app = FastAPI(title="Mezbon")


@app.get("/health")
def report_health() -> dict[str, str]:
    return {"status": "ok"}
