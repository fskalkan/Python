from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {"Data" : {"name":"fskalkan"}}

@app.get("/about")
def about():
    return {"Data" : "name : page about."}