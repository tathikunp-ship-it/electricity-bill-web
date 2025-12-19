from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import io

app = FastAPI(title="Electricity Bill API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if file.filename.endswith(".csv"):
        content = await file.read()
        df = pd.read_csv(io.BytesIO(content))

        return {
            "rows": len(df),
            "columns": list(df.columns),
            "preview": df.head(5).to_dict()
        }

    return {"message": "รองรับเฉพาะไฟล์ CSV ในตอนนี้"}

