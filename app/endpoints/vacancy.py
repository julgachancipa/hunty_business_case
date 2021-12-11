from fastapi import APIRouter, Response, status
from starlette.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND
from typing import List

from config.db import conn
from models.vacancy import vacancies
from models.company import companies
from schemas.vacancy import Vacancy
from schemas.full_vacancy_info import FullVacancyInfo

from settings import Settings

settings = Settings()

vacancy_router = APIRouter(prefix=f"{settings.BASE_API_PREFIX}/vacancy")


@vacancy_router.get("/all", tags=["Vacancy"], response_model=List[Vacancy])
async def get_all_vacancies():
    return conn.execute(vacancies.select()).fetchall()


@vacancy_router.get("/{id}", tags=["Vacancy"], response_model=Vacancy)
async def get_by_id(id: int):
    return conn.execute(vacancies.select().where(vacancies.c.id == id)).first()


@vacancy_router.get("/{id}/company", tags=["Vacancy"], response_model=FullVacancyInfo)
async def get_by_id_with_comapy_info(id: int):
    try:
        vacancy = conn.execute(vacancies.select().where(vacancies.c.id == id)).first()
        company_id = conn.execute(
            vacancies.select()
            .with_only_columns(vacancies.c.company_id)
            .where(vacancies.c.id == id)
        ).first()
        company_id = company_id[0]
        company = conn.execute(
            companies.select().where(companies.c.id == company_id)
        ).first()
        return {"vacancy": vacancy, "company": company}
    except:
        return Response(status_code=HTTP_404_NOT_FOUND)


@vacancy_router.post("/", tags=["Vacancy"], response_model=Vacancy)
async def create_vacancy(vacancy: Vacancy):
    new_vacancy = vacancy.dict(exclude_none=True)
    result = conn.execute(vacancies.insert().values(new_vacancy))

    company_id = new_vacancy.get("company_id")

    if company_id:
        company = conn.execute(
            companies.select().where(companies.c.id == company_id)
        ).first()
        if not company:
            conn.execute(companies.insert().values({"id": company_id}))
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


@vacancy_router.delete(
    "/{id}", tags=["Vacancy"], status_code=status.HTTP_204_NO_CONTENT
)
async def delete_by_id(id: int):
    conn.execute(vacancies.delete().where(vacancies.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)
