from fastapi import FastAPI


app = FastAPI()


@app.get("/hello")
def read_hello():
	return {"message": "hello"}


@app.get("/")
def read_root():
	return {"status": "ok"}