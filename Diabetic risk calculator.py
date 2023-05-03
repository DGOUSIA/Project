import tkinter as tk

def calculate_risk():
    age = int(age_entry.get())
    bmi = float(bmi_entry.get())
    family_history = int(family_history_var.get())
    blood_pressure = int(blood_pressure_var.get())
    cholesterol = int(cholesterol_var.get())
    risk_score = 0
    
    if age >= 30 and age <= 39:
        risk_score += 1
    elif age >= 40 and age <= 49:
        risk_score += 2
    elif age >= 50 and age <= 59:
        risk_score += 3
    elif age >= 60:
        risk_score += 4
        
    if bmi >= 25 and bmi <= 29.9:
        risk_score += 1
    elif bmi >= 30 and bmi <= 34.9:
        risk_score += 2
    elif bmi >= 35 and bmi <= 39.9:
        risk_score += 3
    elif bmi >= 40:
        risk_score += 4
        
    risk_score += family_history
    risk_score += blood_pressure
    risk_score += cholesterol
    
    if risk_score <= 5:
        result = "Low risk"
    elif risk_score >= 6 and risk_score <= 8:
        result = "Moderate risk"
    else:
        result = "High risk"
    
    result_label.config(text=result)

# Create a window
window = tk.Tk()
window.title("Diabetic Risk Calculator")

# Create input fields
age_label = tk.Label(text="Age:")
age_label.grid(column=0, row=0)
age_entry = tk.Entry(width=10)
age_entry.grid(column=1, row=0)

bmi_label = tk.Label(text="BMI:")
bmi_label.grid(column=0, row=1)
bmi_entry = tk.Entry(width=10)
bmi_entry.grid(column=1, row=1)

family_history_label = tk.Label(text="Family history:")
family_history_label.grid(column=0, row=2)
family_history_var = tk.IntVar()
family_history_check = tk.Checkbutton(text="Yes", variable=family_history_var)
family_history_check.grid(column=1, row=2)

blood_pressure_label = tk.Label(text="Blood pressure:")
blood_pressure_label.grid(column=0, row=3)
blood_pressure_var = tk.IntVar()
blood_pressure_check = tk.Checkbutton(text="Yes", variable=blood_pressure_var)
blood_pressure_check.grid(column=1, row=3)

cholesterol_label = tk.Label(text="Cholesterol:")
cholesterol_label.grid(column=0, row=4)
cholesterol_var = tk.IntVar()
cholesterol_check = tk.Checkbutton(text="Yes", variable=cholesterol_var)
cholesterol_check.grid(column=1, row=4)

# Create a button to calculate
calculate_button = tk.Button(text="Calculate", command=calculate_risk)
calculate_button.grid(column=1, row=5)

# Create a label to display the result
result_label = tk.Label(text="")
result_label.grid(column=0, row=6, columnspan=2)

# Run the window
window.mainloop()
