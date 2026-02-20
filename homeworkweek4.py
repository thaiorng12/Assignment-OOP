Age=int(input("Please input your age : "))
Anual_income=int(input("Please input your Annual income : "))
Credit_Score=int(input("Please input your Credit Score : "))
if Age <=20 :
    print("Review Required: Application Age Too Low. ")
elif Age > 25 and Anual_income > 50000 :
    print("Approved: High Tier Loan. ")
elif Credit_Score >= 650 or Anual_income > 30000 : 
    print("Approved: Standard Tier Loan.")
else : print("Denied: Eligibility Criteria Not Met. ") 