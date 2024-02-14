
import pytest
from credit_calculator.credit_model import AnnuityCredit
import pandas as pd

class TestAnnuityCredit:
    """
    Using examples from https://www.haushaltsfinanzen.de/finanzmathematik/annuitaeten.php?Annuitaetendarlehen-mit-online-Tilgungsplan-Rechner
    """
    @pytest.fixture
    def credit(self) -> AnnuityCredit:
        return AnnuityCredit(
            duration_years=5,
            interest_rate_commitment_years=-1,
            interest_rate_per_year_percent=5,
            loan_amount=100000,
            purchasing_price=-1,
            repayment_rate_percent=None,
        )

    def test_get_yearly_rate(self, credit: AnnuityCredit):
        assert credit.get_yearly_rate() == pytest.approx(23097.48, 0.01)

    def test_get_repayment_amount(self, credit: AnnuityCredit):
        assert credit.get_repayment_amount(year=1) == pytest.approx(18097.48, 0.01)
        assert credit.get_repayment_amount(year=2) == pytest.approx(19002.35, 0.01)
        assert credit.get_repayment_amount(year=5) == pytest.approx(21997.60, 0.01)

    def test_get_interest_amount(self, credit: AnnuityCredit):
        assert credit.get_interest_amount(year=1) == pytest.approx(5000, 0.01)
        assert credit.get_interest_amount(year=2) == pytest.approx(4095.13, 0.01)
        assert credit.get_interest_amount(year=5) == pytest.approx(1099.88, 0.01)

    def test_get_repayment_plan(self, credit: AnnuityCredit):
        result: pd.DataFrame = credit.get_repayment_plan()
        assert len(result) == credit.duration_years
