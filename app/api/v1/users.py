from fastapi import APIRouter, Body, Path, Query
from app.core.utils.checkid import find_proper_user_id

from data.users import USERS

router = APIRouter(prefix="/users", tags=["users"])
# router = APIRouter()  # Utilisez router, pas app


# GET ALL ALL
@router.get("/users")
async def get_all_users():
    return USERS

# GET USERS BY COMPANY NAME (AS QUERY PARAM)
@router.get("/users/company/name")
async def get_all_users_by_company_name(company_name:str = Query()):
    result = []
    for user in USERS:
        if "company" in user and "name" in user["company"]:
            if company_name.casefold() == user["company"]["name"].casefold():
                result.append(user)
    return result

# GET USERS BY REPRESENTATIVE NAME (AS QUERY PARAM)
@router.get("/users/representative/name")
async def get_all_users_by_representative_name(representative_name:str = Query()):
    result = []
    for user in USERS:
        if "representative" in user and "first_name" in user["representative"] or "last_name" in user["representative"]:
            if representative_name.casefold() == user["representative"]["first_name"].casefold() or representative_name.casefold() == user["representative"]["last_name"].casefold():
                result.append(user)
    return result

# GET USERS BY SUBSCRIPTION PLAN (AS QUERY PARAM)
@router.get("/users/plan")
async def get_all_users_by_subscription_plan(subscription_plan:int = Query()):
    result = []
    for user in USERS:
        if "subscription_plan" in user:
            if subscription_plan == user["subscription_plan"]:
                result.append(user)
    return result

# GET USERS BY STATUS (AS QUERY PARAM)
@router.get("/users/status")
async def get_all_users_by_status(status:int = Query()):
    result = []
    for user in USERS:
        if "status" in user:
            if user.get("status") == status:
                result.append(user)
    return result

# GET USERS BY id (AS PATH PARAM)
@router.get("/user/id/{user_id}")
async def get_user_by_id(user_id:int = Path()):
    for user in USERS:
        if user.get("id") == user_id:
            return user
        
# POST/CREATE USER BY Body
@router.post("/user/create")
async def create_user(user_body = Body()):
    USERS.append(find_proper_user_id(user_body))

# PUT/UPDATE USER BY Body
@router.put("/user/update")
async def update_user(user_body = Body()):
    for i in range(len(USERS)):
        if USERS[i].get("id") == user_body.get("id"):
            USERS[i] = user_body
            
# DELETE USER BY ID AS PATH PARAM
@router.delete("/user/delete/{user_id}")
async def delete_user(user_id:int = Path()):
    for i in range(len(USERS)):
        if USERS[i].get("id") == user_id:
            USERS.pop(i)
            break
        
# PUT/UPDATE USER STATUS
@router.put("/user/update-status/{user_id}")
async def update_user(user_id:int = Path()):
    for user in USERS:
        if user.get("id") == user_id:
            current_status = user.get("status")
            user["status"] = 1 if current_status == 0 else 0
            return user

