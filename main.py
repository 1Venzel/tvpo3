import tkinter as tk

def calculate_mortgage(principal, annual_rate, years):
    monthly_rate = annual_rate / 12 / 100
    months = years * 12
    payment = principal * monthly_rate / (1 - (1 + monthly_rate) ** -months)
    return round(payment, 2)

def calculate():
    try:
        principal = float(entry_principal.get())
        annual_rate = float(entry_rate.get())
        years = int(entry_years.get())
        payment = calculate_mortgage(principal, annual_rate, years)
        label_result.config(text=f"Monthly Payment: {payment} USD")
    except ValueError:
        label_result.config(text="Invalid input! Please enter numeric values.")

# GUI setup
root = tk.Tk()
root.title("Mortgage Calculator")

tk.Label(root, text="Loan Amount (USD):").grid(row=0, column=0)
entry_principal = tk.Entry(root)
entry_principal.grid(row=0, column=1)

tk.Label(root, text="Annual Interest Rate (%):").grid(row=1, column=0)
entry_rate = tk.Entry(root)
entry_rate.grid(row=1, column=1)

tk.Label(root, text="Loan Term (years):").grid(row=2, column=0)
entry_years = tk.Entry(root)
entry_years.grid(row=2, column=1)

tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2)

label_result = tk.Label(root, text="")
label_result.grid(row=4, column=0, columnspan=2)

root.mainloop()
