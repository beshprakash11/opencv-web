from fastapi import FastAPI, File, UploadFile
import uvicorn
from imgproc import read_image

app = FastAPI()

@app.get('/')
def index():
    return {'data' : 'IPPR'}

@app.post('/api/image')
async def imgUpload(file: bytes = File(...)):
    read_image.pre_process(file)
    return {'image':'loaded successfully'}

@app.get('/api/network/image')
async def readImage():
    return {'image' : '<img src0'}

# defining host and port
if __name__ == '__main__':
    uvicorn.run(app) # , host='0.0.0.0', port=8005)
