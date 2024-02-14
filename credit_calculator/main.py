
import math
from typing import Iterable, Set, Dict, Final

from credit_calculator.credit_model import AnnuityCredit
import matplotlib.pyplot as plt
import pandas as pd

# pd.set_option("display.precision", 2)
pd.options.display.float_format = "{:,.2f}".format

loan_amount: Final[float] = 300000
interest_rate_per_year_percent: Final[float] = 4.0

duration_years: Iterable[int] = range(10, 31, 1)


monthly_rates: Dict[int, float] = {}
for duration_year in duration_years: 
    credit: AnnuityCredit = AnnuityCredit(
        duration_years=duration_year,
        interest_rate_commitment_years=-1,
        interest_rate_per_year_percent=interest_rate_per_year_percent,
        loan_amount=loan_amount,
        purchasing_price=-1,
        repayment_rate_percent=None,
    )
    monthly_rates[duration_year] = credit.get_monthly_rate()
    # if duration_year == min(duration_years) or duration_year == max(duration_years):
    # if duration_year % 10 == 0:
    repayment_plan: pd.DataFrame = credit.get_repayment_plan()
    for column in ["repayment_amount_euro", "interest_amount_euro", "payment_yearly_euro"]:
        print(f"Sum {column}: {repayment_plan[column].sum():,.2f}")


print("Monthly rates:")
print(monthly_rates)

plt.scatter(monthly_rates.keys(), monthly_rates.values())
plt.title(f"Annuitätsdarlehen (Monatsrate bleibt gleich) \n"
          f"Darlehen: {loan_amount:,}€, Sollzins p.a.: {interest_rate_per_year_percent}%")
plt.ylim(ymin=500)
plt.ylabel("Monatsrate (€)")
plt.xlabel("Kreditdauer (Jahre)")

xint = range(min(monthly_rates.keys()), math.ceil(max(monthly_rates.keys()))+1, 2)
plt.xticks(xint)

plt.savefig('duration_years_to_monthly_rate.png')



monthly_loan_installments: Iterable[float] = range(1000, 3000, 50)


