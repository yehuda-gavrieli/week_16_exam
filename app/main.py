from fastapi import FastAPI
import dal

app = FastAPI()

@app.get("/employees/engineering/high-salary")
def engineering_high_salary():
    return dal.get_engineering_high_salary_employees()

@app.get("/employees/by-age-and-role")
def by_age_role():
    return dal.get_employees_by_age_and_role()

@app.get("/employees/top-seniority")
def top_seniority():
    return dal.get_top_seniority_employees_excluding_hr()

@app.get("/employees/age-or-seniority")
def age_seniority():
    return dal.get_employees_by_age_or_seniority()

@app.get("/employees/managers/excluding-departments")
def managers_no_sales_marketing():
    return dal.get_managers_excluding_departments()

@app.get("/employees/by-lastname-and-age")
def lastname_age():
    return dal.get_employees_by_lastname_and_age()