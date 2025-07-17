from typing import List
from app.model.classes import User, Company, Representative

USERS: List[User] = [    
    User(
        id= 1,
        company = Company(
                name= "DATUM",
                email= "contact@datum-solution.com",
                contact= "+237699999999",
                location= "Yaounde",
                domain="datum-solution.com"
            ),
        representative = Representative(
                first_name= "John",
                last_name= "Dow",
                email= "j.dow@datum-solution.com",
                contact= "+237677777777",
                location= "Yaounde",
            ),
        business_categories= [
            "Teaching",
            "IT",
            "Consulting"
        ],
        registration_date= "2025-07-17T13:00:00",
        subscription_plan= 1,
        status= 1
    ),
     User(
        id= 2,
        company = Company(
                name= "SAAS",
                email= "",
                contact= "",
                location= "",
                domain="saas.com"
            ),
        representative = Representative(
                first_name= "Donald",
                last_name= "",
                email= "donald@email.com",
                contact= "+49123456789",
                location= "Berlin",
            ),
        business_categories= [
            "Articficial Intelligence",
        ],
        registration_date= "2022-07-17T13:00:00",
        subscription_plan= 2,
        status= 0
    )
]