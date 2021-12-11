from fastapi import APIRouter, Response, status
from starlette.status import HTTP_204_NO_CONTENT
from typing import List

from config.db import conn
from models.vacancy import vacancies
from schemas.vacancy import Vacancy

from settings import Settings

settings = Settings()

vacancy_router = APIRouter(prefix=f"{settings.BASE_API_PREFIX}/user")


@vacancy_router.get("/all", tags=["Vacancy"], response_model=List[Vacancy])
async def get_all_vacancies():
    return conn.execute(vacancies.select()).fetchall()


@vacancy_router.get("/{id}", tags=["Vacancy"], response_model=Vacancy)
async def get_by_id(id: int):
    return conn.execute(vacancies.select().where(vacancies.c.id == id)).first()


@vacancy_router.post("/", tags=["Vacancy"], response_model=Vacancy)
async def create_vacancy(vacancy: Vacancy):
    new_vacancy = vacancy.dict(exclude_none=True)
    result = conn.execute(vacancies.insert().values(new_vacancy))
    return conn.execute(
        vacancies.select().where(vacancies.c.id == result.lastrowid)
    ).first()


@vacancy_router.put("/{id}", tags=["Vacancy"], response_model=Vacancy)
async def update_by_id(id: int, vacancy: Vacancy):
    update_vacancy = vacancy.dict(exclude_none=True)
    if id in vacancy:
        update_vacancy.pop("id")
    conn.execute(vacancies.update().values(update_vacancy).where(vacancies.c.id == id))
    return conn.execute(vacancies.select().where(vacancies.c.id == id)).first()


@vacancy_router.delete("/{id}", tags=["Vacancy"], status_code=status.HTTP_204_NO_CONTENT)
async def delete_by_id(id: int):
    conn.execute(vacancies.delete().where(vacancies.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)
