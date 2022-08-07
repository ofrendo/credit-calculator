
import math
from typing import Iterable, Set, Dict, Final

from credit_calculator.credit_model import AnnuityCredit
import matplotlib.pyplot as plt

loan_amount: Final[float] = 400000
interest_rate_per_year_percent: Final[float] = 3.0

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
    
    
print(monthly_rates)

plt.scatter(monthly_rates.keys(), monthly_rates.values())
plt.title(f"Annuitätsdarlehen (Monatsrate bleibt gleich) \n"
          f"Darlehen: {loan_amount:,}€, Sollzins p.a.: {interest_rate_per_year_percent}%")
plt.ylim(ymin=1000)
plt.ylabel("Monatsrate (€)")
plt.xlabel("Kreditdauer (Jahre)")

xint = range(min(monthly_rates.keys()), math.ceil(max(monthly_rates.keys()))+1, 2)
plt.xticks(xint)

plt.savefig('duration_years_to_monthly_rate.png')



monthly_loan_installments: Iterable[float] = range(1000, 3000, 50)


