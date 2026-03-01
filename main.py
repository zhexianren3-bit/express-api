from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root(): return {"msg": "物流API"}
@app.get("/trace")
def trace(no: str = ""):
    return {"success": True, "status": "运输中", "location": "北京"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
