from connection import collection

def get_engineering_high_salary_employees():
    query = {
        "job_role.department": "Engineering",
        "salary": {"$gt": 65000}
    }
    projection = {"employee_id": 1, "name": 1, "salary": 1, "_id": 0}
    return list(collection.find(query, projection))


def get_employees_by_age_and_role():
    query = {
        "age": {"$gte": 30, "$lte": 45},
        "job_role.title": "Engineer"
    }
    return list(collection.find(query, {"_id": 0}))


def get_top_seniority_employees_excluding_hr():
    query = {"job_role.department": {"$ne": "HR"}}
    return list(collection.find(query, {"_id": 0}).sort("years_at_company", -1).limit(7))
