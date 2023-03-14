from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def index():
    return {'data' : 'firest img processing'}