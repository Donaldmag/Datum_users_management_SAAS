from fastapi import APIRouter, Body, Path, Query, HTTPException
from app.core.utils.checkid import find_proper_user_id
from app.model.classes import User, UserValidation
from starlette import status

from data.users import USERS

router = APIRouter(prefix="/users", tags=["users"])

# GET ALL ALL
@router.get("/users", status_code=status.HTTP_200_OK)
async def get_all_users():
    return USERS

# GET USERS BY COMPANY NAME (AS QUERY PARAM)
@router.get("/users/company/name", status_code=status.HTTP_200_OK)
async def get_all_users_by_company_name(company_name:str = Query()):
    result = []
    for user in USERS:
        if company_name.casefold() == user.company.name.casefold():
            result.append(user)
    return result

# GET USERS BY REPRESENTATIVE NAME (AS QUERY PARAM)
@router.get("/users/representative/name", status_code=status.HTTP_200_OK)
async def get_all_users_by_representative_name(representative_name:str = Query()):
    result = []
    for user in USERS:
        if representative_name.casefold() == user.representative.first_name.casefold() or representative_name.casefold() == user.representative.last_name.casefold():
            result.append(user)
    return result

# GET USERS BY SUBSCRIPTION PLAN (AS QUERY PARAM)
@router.get("/users/plan", status_code=status.HTTP_200_OK)
async def get_all_users_by_subscription_plan(subscription_plan:int = Query(ge=1, le=3)):
    result = []
    for user in USERS:
        if user.subscription_plan == subscription_plan:
            result.append(user)
    return result

# GET USERS BY STATUS (AS QUERY PARAM)
@router.get("/users/status", status_code=status.HTTP_200_OK)
async def get_all_users_by_status(status:int = Query(ge=0, le=1)):
    result = []
    for user in USERS:
        if user.status == status:
            result.append(user)
    return result

# GET USERS BY id (AS PATH PARAM)
@router.get("/user/id/{user_id}", status_code=status.HTTP_200_OK)
async def get_user_by_id(user_id:int = Path(gt=0)):
    for user in USERS:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")
        
# POST/CREATE USER BY Body
@router.post("/user/create", status_code=status.HTTP_201_CREATED)
async def create_user(user_body:UserValidation = Body()):
    new_user = User(**user_body.model_dump())
    USERS.append(find_proper_user_id(new_user))

# PUT/UPDATE USER BY Body
@router.put("/user/update", status_code=status.HTTP_204_NO_CONTENT)
async def update_user(user_body:UserValidation = Body()):
    user_changed = False
    for i in range(len(USERS)):
        if USERS[i].id == user_body.id:
            user_changed = True
            USERS[i] = User(**user_body.model_dump())
    if not user_changed:
        raise HTTPException(status_code=404, detail="User not found")
            
# DELETE USER BY ID AS PATH PARAM
@router.delete("/user/delete/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id:int = Path(gt=0)):
    user_changed = False
    for i in range(len(USERS)):
        if USERS[i].id == user_id:
            user_changed = True
            USERS.pop(i)
            break
    if not user_changed:
        raise HTTPException(status_code=404, detail="User id not found")
        
# PUT/UPDATE USER STATUS
@router.put("/user/update-status/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_user(user_id:int = Path(gt=0)):
    user_changed = False
    for user in USERS:
        if user.id == user_id:
            current_status = user.status
            user_changed = True
            user.status = 1 if current_status == 0 else 0
            return user
    if not user_changed:
        raise HTTPException(status_code=304, detail="Nothing modified")
