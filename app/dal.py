from connection import employees_col


def get_engineering_high_salary_employees():
    query = {"job_role.department": "Engineering",
             "salary": {"$gt": 65000}}
    projection = {"employee_id": 1, "name": 1, "salary": 1, "_id": 0}
    return list(employees_col.find(query, projection))

def get_employees_by_age_and_role():
    query = {"age": {"$gte": 30, "$lte": 45},
             "job_role.title": {"$in": ["Engineer", "Specialist"]}}
    return list(employees_col.find(query, {"_id": 0}))

def get_top_seniority_employees_excluding_hr():
    query = {"job_role.department": {"$ne": "HR"}}
    return list(employees_col.find(query, {"_id": 0}).sort("years_at_company", -1).limit(7))

def get_employees_by_age_or_seniority():
    query = {"$or": 
             [{"age": {"$gt": 50}},
              {"years_at_company": {"$lt": 3}}]}
    projection = {"employee_id": 1, "name": 1, "age": 1, "years_at_company": 1, "_id": 0}
    return list(employees_col.find(query, projection))

def get_managers_excluding_departments():
    query = {"job_role.title": "Manager",
             "job_role.department": {"$nin": ["Sales", "Marketing"]}}
    return list(employees_col.find(query, {"_id": 0}))

def get_employees_by_lastname_and_age():
    query = {"name": {"$regex": r"(Nelson|Wright)$", "$options": "i"},
             "age": {"$lt": 35}}
    projection = {"name": 1, "age": 1, "job_role.department": 1, "_id": 0}
    return list(employees_col.find(query, projection))
