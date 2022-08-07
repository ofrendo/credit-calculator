from pydantic import BaseModel
from typing import Optional

class Credit(BaseModel):
    purchasing_price: float  # Kaufpreis
    loan_amount: float  # Darlehensbeitrag
    interest_rate_commitment_years: float = 10  # Sollzins bindung (Jahre)
    interest_rate_per_year_percent: float = 2.5  # Sollzins (set by bank)  TODO effektivzins vs nominalzins
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
        print(f"Compound interest (interest over duration) for {self.duration_years} years: {interest_over_duration}."
              f" Bank is paid: ")
        return self.loan_amount * (interest_rate * interest_over_duration / (interest_over_duration - 1)) 

    def get_monthly_rate(self) -> float:
        return self.get_yearly_rate() / 12  # TODO recheck

    def get_repayment_amount_for_year(self, year: int) -> float:
        """
        How much is repayed of the credit for year x?
        """
        pass

    def get_interest_amount_for_year(self, year: int) -> float:
        """
        How much is bank payed for year x?
        """
        pass

class InstallmentCredit(Credit):
    # ratenkredit: zins für gesamte laufzeit festgelegt, annuität ist variabel und nimmt über zeit ab
    # https://www.haushaltsfinanzen.de/finanzmathematik/ratenkredit.php?Ratenkredit-mit-online-Tilgungsplan-Rechner
    pass

class CreditSimulationResult(BaseModel):
    pass
