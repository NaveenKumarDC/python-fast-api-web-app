from fastapi import Depends, FastAPI

from dependencies import get_query_token, get_token_header
from routers.internal import admin
from routers import items, users, EmployeeRouter

app = FastAPI(dependencies=[Depends(get_query_token)])


app.include_router(users.router)
app.include_router(items.router)
app.include_router(EmployeeRouter.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    return {"message": "Hello Biggef rd "
                       ""
                       ""
                       ""
                       "r Applications!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)