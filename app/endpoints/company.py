from fastapi import APIRouter, Response, status
from starlette.status import HTTP_204_NO_CONTENT
from typing import List

from config.db import conn
from models.company import companies
from schemas.company import Company

from settings import Settings

settings = Settings()

company_router = APIRouter(prefix=f"{settings.BASE_API_PREFIX}/company")


@company_router.get("/all", tags=["Company"], response_model=List[Company])
async def get_all_companies():
    return conn.execute(companies.select()).fetchall()


@company_router.get("/{id}", tags=["Company"], response_model=Company)
async def get_by_id(id: int):
    return conn.execute(companies.select().where(companies.c.id == id)).first()


@company_router.post("/", tags=["Company"], response_model=Company)
async def create_company(company: Company):
    new_company = company.dict(exclude_none=True)
    result = conn.execute(companies.insert().values(new_company))
    return conn.execute(
        companies.select().where(companies.c.id == result.lastrowid)
    ).first()


@company_router.put("/{id}", tags=["Company"], response_model=Company)
async def update_by_id(id: int, company: Company):
    update_company = company.dict(exclude_none=True)
    if id in company:
        update_company.pop("id")
    conn.execute(companies.update().values(update_company).where(companies.c.id == id))
    return conn.execute(companies.select().where(companies.c.id == id)).first()


@company_router.delete(
    "/{id}", tags=["Company"], status_code=status.HTTP_204_NO_CONTENT
)
async def delete_by_id(id: int):
    conn.execute(companies.delete().where(companies.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)
