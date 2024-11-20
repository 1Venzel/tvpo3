import tkinter as tk


def calculate_mortgage(amount, rate, years):
    """
    Рассчитывает ежемесячный платёж по ипотеке.
    :param amount: Сумма кредита.
    :param rate: Годовая процентная ставка (в процентах).
    :param years: Срок кредита (в годах).
    :return: Ежемесячный платёж.
    """
    monthly_rate = rate / 12 / 100
    months = years * 12
    monthly_payment = amount * monthly_rate / (1 - (1 + monthly_rate) ** -months)
    return round(monthly_payment, 2)


def calculate():
    """
    Функция для обработки ввода пользователя и отображения результата.
    """
    try:
        principal = float(entry_principal.get())
        annual_rate = float(entry_rate.get())
        years = int(entry_years.get())
        payment = calculate_mortgage(principal, annual_rate, years)
        label_result.config(text=f"Monthly Payment: {payment} USD")
    except ValueError:
        label_result.config(text="Invalid input! Please enter numeric values.")


# Запуск GUI только при выполнении файла напрямую
if __name__ == "__main__":
    # GUI setup
    root = tk.Tk()
    root.title("Mortgage Calculator")

    # Ввод суммы кредита
    tk.Label(root, text="Loan Amount (USD):").grid(row=0, column=0, padx=5, pady=5)
    entry_principal = tk.Entry(root)
    entry_principal.grid(row=0, column=1, padx=5, pady=5)

    # Ввод процентной ставки
    tk.Label(root, text="Annual Interest Rate (%):").grid(row=1, column=0, padx=5, pady=5)
    entry_rate = tk.Entry(root)
    entry_rate.grid(row=1, column=1, padx=5, pady=5)

    # Ввод срока кредита
    tk.Label(root, text="Loan Term (years):").grid(row=2, column=0, padx=5, pady=5)
    entry_years = tk.Entry(root)
    entry_years.grid(row=2, column=1, padx=5, pady=5)

    # Кнопка расчёта
    tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2, pady=10)

    # Метка для отображения результата
    label_result = tk.Label(root, text="", fg="blue")
    label_result.grid(row=4, column=0, columnspan=2, pady=5)

    # Запуск основного цикла приложения
    root.mainloop()
