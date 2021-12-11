from .company import Company
from .vacancy import Vacancy

from pydantic import BaseModel


class FullVacancyInfo(BaseModel):
    company: Company
    vacancy: Vacancy
