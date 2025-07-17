from datetime import datetime
from typing import List
from pydantic import BaseModel

class Company(BaseModel):
    name: str
    email: str
    contact: str
    location: str
    domain: str
    
class Representative(BaseModel):
    first_name: str
    last_name: str
    email: str
    contact: str
    location: str
    
class User(BaseModel):
    id: int
    company: Company
    representative: Representative
    business_categories: List[str]
    registration_date: datetime
    subscription_plan: int
    status: int
    def __ini__(self, id, company, representative, business_categories, registration_date, subscription_plan, status):
        self.id = id
        self.company = company
        self.representative = representative
        self.business_categories = business_categories
        self.registration_date = registration_date
        self.subscription_plan = subscription_plan
        self.status = status