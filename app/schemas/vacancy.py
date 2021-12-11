from typing import Optional
from pydantic import BaseModel


class Vacancy(BaseModel):
    id: Optional[int]
    position_name: Optional[str]
    vacancy_link: Optional[str]
    company_id: Optional[int]
    salary: Optional[float]
    skills: Optional[str]
    min_experience: Optional[int]
    max_experience: Optional[int]
