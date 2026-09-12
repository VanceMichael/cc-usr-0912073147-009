from fastapi import FastAPI

app = FastAPI(title="合同退费核算")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/calculations", status_code=202)
def calculate(payload: dict) -> dict[str, str]:
    if not payload.get("contract_id"):
        return {"status": "rejected", "reason": "合同编号不能为空"}
    return {"status": "queued"}

