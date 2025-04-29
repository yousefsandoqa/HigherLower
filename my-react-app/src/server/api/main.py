from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.api.user_router import router as user_router
from server.api.career_router import router as career_router
from server.api.season_router import router as season_router

app = FastAPI(root_path="/")
app.include_router(user_router)
app.include_router(career_router)
app.include_router(season_router)

origins = [
    "http://127.0.0.1/",
    "http://localhost:5173", 
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def get_test():
    return {"message": "CSE412 Project",
            "members": "Omar, Samik, Zuhayr, Yousef"}    