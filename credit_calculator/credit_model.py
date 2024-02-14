from pydantic import BaseModel
from typing import Optional
import pandas as pd


class Credit(BaseModel):
    purchasing_price: float  # Kaufpreis
    loan_amount: float  # Darlehensbeitrag
    interest_rate_commitment_years: float = 10  # Sollzins bindung (Jahre)
    # Sollzins (set by bank). Sollzins = Nominalzins. Effektivzins = effektiver Jahreszins = Sollzins + Kosten + Gebühren
    # https://www.allianz.de/recht-und-eigentum/baufinanzierung/annuitaetendarlehen/#:~:text=Ein%20Annuit%C3%A4tendarlehen%20(selten%20auch%20Annuit%C3%A4tenkredit,einem%20Tilgungsanteil%20(R%C3%BCckzahlung)%20zusammen.
    interest_rate_per_year_percent: float = 2.5
    repayment_rate_percent: Optional[float]  # Tilgungssatz
    duration_years: Optional[int]  # Wann ist Kredit bezahlt

    def get_yearly_rate(self) -> float:
        raise NotImplementedError("Use subclass!")


class AnnuityCredit(Credit):
    # annuitätendarlehen: höhe der annuität bleibt gleich
    # Anteil der Rate: zins vs tilgungszahlung ändert sich über zeit
    # https://www.haushaltsfinanzen.de/finanzmathematik/annuitaeten.php?Annuitaetendarlehen-mit-online-Tilgungsplan-Rechner
    
    def get_credit_sum(self) -> float:
        """
        Kreditbetrag, "ursprüngliche Kreditsumme"
        """
        return

    def get_yearly_rate(self) -> float:
        """
        Annuität berechnen
        """
        interest_rate: float = self.interest_rate_per_year_percent / 100  # Zinssatz
        interest_over_duration: float = (1 + interest_rate)**self.duration_years  # zinseszins, compound interest
        print(f"Compound interest (interest over duration) for {self.duration_years} years: {interest_over_duration:.2f}%.")
        return self.loan_amount * (interest_rate * interest_over_duration / (interest_over_duration - 1))

    def get_monthly_rate(self) -> float:
        return self.get_yearly_rate() / 12  # TODO recheck

    def get_repayment_amount(self, year: int) -> float:
        """
        How much is repayed of the credit for year x? This is variable and increases each year.
        Tilgungsrate (in %)
        """
        interest_rate: float = self.interest_rate_per_year_percent / 100  # Zinssatz
        return (interest_rate * (1+interest_rate)**(year-1)) / ((1+interest_rate)**self.duration_years - 1) * self.loan_amount

    def get_interest_amount(self, year: int) -> float:
        """
        How much is bank payed for year x?
        """
        interest_rate: float = self.interest_rate_per_year_percent / 100  # Zinssatz
        return (interest_rate * ((1+interest_rate)**self.duration_years - (1+interest_rate)**(year-1))) / ((1 + interest_rate)**self.duration_years -1) * self.loan_amount

    def get_repayment_plan(self) -> pd.DataFrame:
        repayment_amounts: List[float] = []
        interest_amounts: List[float] = []
        payments: List[float] = []
        remaining_loan_amounts: List[float] = []
        remaining_loan_amount: float = self.loan_amount
        for year in range(1, self.duration_years+1):
            repayment_amount: float = self.get_repayment_amount(year)
            repayment_amounts.append(repayment_amount)
            interest_amount: float = self.get_interest_amount(year)
            interest_amounts.append(interest_amount)
            payment: float = repayment_amount + interest_amount
            payments.append(payment)
            remaining_loan_amount -= repayment_amount
            remaining_loan_amounts.append(remaining_loan_amount)

        result: Dict[str, List[float]] = {
            "year": list(range(1, self.duration_years+1)),
            "repayment_amount_euro": repayment_amounts,
            "interest_amount_euro": interest_amounts,
            "payment_yearly_euro": payments,
            "remaining_loan_amount_euro": remaining_loan_amounts
        }
        return pd.DataFrame.from_dict(result)



class InstallmentCredit(Credit):
    # ratenkredit: zins für gesamte laufzeit festgelegt, annuität ist variabel und nimmt über zeit ab
    # https://www.haushaltsfinanzen.de/finanzmathematik/ratenkredit.php?Ratenkredit-mit-online-Tilgungsplan-Rechner
    pass


class CreditSimulationResult(BaseModel):
    pass
