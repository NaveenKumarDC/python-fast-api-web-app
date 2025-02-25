from fastapi import APIRouter, Depends, HTTPException
from dependencies import get_token_header
from core.MongoDataBase import db
from model import Employee


router = APIRouter(
    prefix="/employee",
    tags=["employee"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.post("/create_employee/", response_model= None)
async def create_employee(email: str) -> Employee:
    """
    Create a new employee.
    Args:
        emp (Employee): the employee details to be created
    Returns:
        Employee: Employee Json object
    """
    # Check if the email already exists in the database
    existing_employee_details = db.employee.find_one({"email": email})
    if not existing_employee_details:
        # raise HTTPException(status_code=404, detail="Employee not found")
        result = db.employee.insert_one({"email": email})
        employee_details = db.employee.find_one({"_id": result.inserted_id})
        if employee_details:
            employee_details["_id"] = str(employee_details["_id"])
        return employee_details
    else:
        # return {"message": f"Employee with email {email} has been created"}
        if existing_employee_details:
            existing_employee_details["_id"] = str(existing_employee_details["_id"])
        return existing_employee_details
    # inserted_email = str(employee_details["email"])
    # return f"Employee with email {inserted_email} has been created"
    # return {**employee_details, "id": str(employee_details["_id"])}
    # return {"message": f"Employee with email {inserted_email} has been created"}


@router.get("/get_employee/")
async def get_all_employees():
    """"
    Get list of all employees
    Args: None
    Returns: A list of employee records as Json objects
    """
    #Query the database to retrieve all employees
    employees = db.employee.find({})

    #if no employees found, return an empty list
    if not employees:
        return []

    for employee in employees:
        employee[ "_id"] = str(employee["_id"])

    return employees

@router.get("/get_employee/{employee_id}")
async def get_employee(employee_id: int):
    """"
    Get employee details
    Args:
        employee_id (int): the employee id
    
    Returns:
        JSON: JSON response object with employee details
    """
    employee = db.employee.find_one({"_id": employee_id})
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@router.get("/get_employee_by_email/{email}")
async def get_employee(email: str):
    """"
    Get employee details
    Args:
        email (str): the employee email id

    Returns:
        JSON: JSON response object with employee details matching with the given email
    """
    employee = db.employee.find_one({"email": email})
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    employee[ "_id"] = str(employee["_id"])
    return employee

# @router.put("/update_employee_by_email/{email}")
# async def update_employee(email: str, updated_employee: Employee):
#     """"
#     Update employee details
#     Args:
#         email (str): the employee email id
#         updated_employee (Employee): the employee details to be updated
#    Returns:
#         JSON: JSON response object with employee details
#     """
#     existing_employee = db.employee.find_one({"email": email})
#     if not existing_employee:
#         raise HTTPException(status_code=404, detail="Employee not found")
#
#     existing_employee_id = existing_employee.get('_id')
#     if existing_employee_id:
#         existing_employee_id = str(existing_employee_id)
#
#     # Remove the _id field from the updated_employee dictionary
#     updated_employee_dict = updated_employee.dict()
#     updated_employee_dict.pop('_id', None)
#
#     # Update the employee with the provided email
#     db.employee.update_one({"_id": existing_employee_id}, updated_employee_dict)
#
#     # Retrieve the updated employee from the database
#     updated_employee_doc = db.items.find_one({ "email" : email})
#     updated_employee_doc.pop('_id', None)
#     print(updated_employee_doc)
#     return f"Employee with email {updated_employee_doc['email']} has been updated"

@router.delete("/delete_employee/{employee_id}")
async def delete_employee(employee_id: int):
    """
    Delete employee details
    Args:
    employee_id (int): the employee id
    Returns:
        JSON: JSON response object with employee details
    """
    employee = db.employee.find_one({"_id": employee_id})
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    db.employee.delete_one({"_id": employee_id})
    return f"Employee with id {employee_id} has been deleted"