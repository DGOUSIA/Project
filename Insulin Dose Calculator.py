import tkinter as tk
import csv
import matplotlib.pyplot as plt

class DiabeticCalculator:
    def __init__(self, master, file_path):
        self.master = master
        self.file_path = file_path
        master.title("Diabetic Calculator")

        # Create Labels
        self.label_weight = tk.Label(master, text="Weight (lbs):")
        self.label_weight.grid(row=0, column=0)

        self.label_carbs = tk.Label(master, text="Carbohydrates (g):")
        self.label_carbs.grid(row=1, column=0)

        self.label_bs = tk.Label(master, text="Blood Sugar Target (mg/dL):")
        self.label_bs.grid(row=2, column=0)

        self.label_result = tk.Label(master, text="")
        self.label_result.grid(row=4, column=0)

        # Create Entries
        self.entry_weight = tk.Entry(master)
        self.entry_weight.grid(row=0, column=1)

        self.entry_carbs = tk.Entry(master)
        self.entry_carbs.grid(row=1, column=1)

        self.entry_bs = tk.Entry(master)
        self.entry_bs.grid(row=2, column=1)

        # Create Button
        self.button_calculate = tk.Button(master, text="Calculate Insulin Dosage", command=self.calculate)
        self.button_calculate.grid(row=3, column=0)

    def calculate(self):
        weight = float(self.entry_weight.get())
        carbs = float(self.entry_carbs.get())
        bs_target = float(self.entry_bs.get())

        insulin_dosage = carbs / 10 + (weight / 4) - (bs_target / 100)

        result_text = "Insulin Dosage: {:.2f} units".format(insulin_dosage)
        self.label_result.config(text=result_text)

        # Write data to CSV file
        with open(self.file_path, mode='a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([weight, carbs, bs_target, insulin_dosage])

        # Create graph
        carbs_list = [10, 20, 30, 40, 50]
        insulin_dose_list = [carbs / 10 + (weight / 4) - (bs_target / 100) for carbs in carbs_list]
        plt.plot(carbs_list, insulin_dose_list)
        plt.title("Carbohydrates vs. Insulin Dose")
        plt.xlabel("Carbohydrates (g)")
        plt.ylabel("Insulin Dose (units)")
        plt.show()

root = tk.Tk()

# Specify file path
file_path = "C:\\Users\\mgows\\OneDrive\\Desktop\\New folder\\diabetic_data.csv"

# Create Diabetic Calculator instance
my_gui = DiabeticCalculator(root, file_path)
root.mainloop()

