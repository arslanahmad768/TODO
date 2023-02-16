from fastapi import FastAPI,APIRouter,status

app = FastAPI()
router = APIRouter()

@app.get("/")
async def root():
    return {"Success":"Welcome to CRUD operation"}


app.include_router(router,tags='[todo]',prefix='/api/todo')

