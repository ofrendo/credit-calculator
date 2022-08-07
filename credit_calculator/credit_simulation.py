from credit_calculator.credit_model import Credit, CreditSimulationResult


class CreditSimulation:
    def __init__(self, credit: Credit):
        self.credit = credit

    def simulate_credit(self) -> CreditSimulationResult:
        """
        Simulate credit until debt is repayed
        """
        # https://www.finanzcheck.de/kredit/monatsrate-berechnen/
        yearly_loan_installment: float = self.credit.get_yearly_rate()  # Darlehensrate, besteht aus Zinsen + Tilgung
        remaining_debt: float = self.credit.loan_amount
        while remaining_debt > 0:
            remaining_debt -= yearly_loan_installment
        
        



