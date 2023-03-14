from fastapi import FastAPI, File, UploadFile
import uvicorn

app = FastAPI()

@app.get('/')
def index():
    return {'data' : 'IPPR'}

@app.post('/api/image')
async def imgUpload(file:UploadFile = File(...)):
    return {'image' : 'sample image'}

# defining host and port
if __name__ == '__main__':
    uvicorn.run(app) # , host='0.0.0.0', port=8005)
