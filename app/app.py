import uvicorn

from fastapi import FastAPI
from starlette.responses import RedirectResponse

from endpoints.vacancy import vacancy_router

app = FastAPI(
    title="Hunty Business Case",
    version="0.1.0",
    openapi_tags=[
        {
            "name": "Vacancy",
            "description": "Vacancy routes"
        }
    ]
)

app.include_router(vacancy_router)


@app.get("/")
async def root():
    return RedirectResponse(url="/docs/")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
