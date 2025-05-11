import requests

# Webhook and token (replace with your real values)
webhook_url = "https://bfhldevapigw.healthrx.co.in/hiring/testWebhook/PYTHON"
access_token = "eyJhbGciOiJIUzI1NiJ9.eyJyZWdObyI6IlJFRzEyMzQ0NyIsIm5hbWUiOiJNYWhhayBNYXRrYXIiLCJlbWFpbCI6Im1haGFrNTg1OTFAZ21haWwuY29tIiwic3ViIjoid2ViaG9vay11c2VyIiwiaWF0IjoxNzQ2OTY0MDQ5LCJleHAiOjE3NDY5NjQ5NDl9.HSPC_HIclYQSve4EGoP3SUHLxEvWg0Z65XB194p9AmE"

final_query = {
    "finalQuery": "SELECT p.amount AS SALARY, CONCAT(e.first_name, ' ', e.last_name) AS NAME, TIMESTAMPDIFF(YEAR, e.dob, CURDATE()) AS AGE, d.department_name AS DEPARTMENT_NAME FROM payments p JOIN employee e ON p.emp_id = e.emp_id JOIN department d ON e.department = d.department_id WHERE DAY(p.payment_time) != 1 ORDER BY p.amount DESC LIMIT 1;"
}


# Authorization Header
headers = {
    "Authorization": access_token,
    "Content-Type": "application/json"
}

# Submit your solution
response = requests.post(webhook_url, json=final_query, headers=headers)

print("Submission Status:", response.status_code)
print("Response Body:", response.text)