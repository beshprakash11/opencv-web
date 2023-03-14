from fastapi import FastAPI, File, UploadFile


app = FastAPI()

@app.get('/')
def index():
    return {'data' : 'IPPR'}

@app.post('/api/image')
async def imgUpload(file:UploadFile = File(...)):
    return {'image' : 'sample image'}
