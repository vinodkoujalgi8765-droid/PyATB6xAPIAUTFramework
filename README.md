# Python API Automation Framework

Hybrid Custom API Automation Framework include the proper folder structure
![Screenshot 2024-08-05 at 08 18 38](https://github.com/user-attachments/assets/3c7d5fe5-207a-42e7-84fe-f4d53354d987)

Tech Stack (what are the different technologies and libraries that you are using )

- Python latest
- Requests - HTTP Requests
- PyTest - Testing Framework
- Reporting - Allure Report, ~PyTest HTML~
- Test Data - CSV, Excel, JSON, Faker ( if you have multiple data that you want to basically test it out,   for example, you want to test a login page with hundreds of usernames and passwords ) CSV is comma seperated values, excel file MS document perserved format. 
- Advance API Testcase - jsonschema
- Parallel Execution - x distribute (xdist)

How to Install Packages  
-pip install requests pytest pytest-html faker allure-pytest jsonschema


How to run your Testcase Parallel
-pip install pytest-xdist 

How to run the Basic Test with Allure report
-pytest tests/tests/crud/test_create_booking.py  --alluredir=allure_result -s
