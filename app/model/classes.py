from enum import Enum
from datetime import datetime
from typing import List, Literal, Optional
from pydantic import BaseModel, EmailStr, Field, conint, constr

class Company(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    contact: Optional[str] = None
    location: Optional[str] = None
    domain: constr(min_length=3)
    
class Representative(BaseModel):
    first_name: constr(min_length=3)
    last_name: constr(min_length=3)
    email: EmailStr
    contact: constr(min_length=6)
    location: constr(min_length=3)
    
class SubscriptionPlanEnum(int, Enum):
    STARTER_PLAN = 1
    BUSINESS_PLAN = 2
    PREMIUM_PLAN = 3


class StatusEnum(int, Enum):
    INACTIVE = 0
    ACTIVE = 1
    
class User(BaseModel):
    id: Optional[int] = Field(default=None, ge=0, description="id not required", nullable=True)
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
        
class UserValidation(BaseModel):
    id: Optional[int] = Field(default=None, ge=0, description="id not required", nullable=True)
    company: Company
    representative: Representative
    business_categories: List[constr(min_length=3)]
    registration_date: datetime
    subscription_plan: SubscriptionPlanEnum
    status: StatusEnum
