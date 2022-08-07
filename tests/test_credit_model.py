
import pytest
from credit_calculator.credit_model import AnnuityCredit


class TestAnnuityCredit:

    def test_get_yearly_rate(self):
        credit: AnnuityCredit = AnnuityCredit(
            duration_years=5,
            interest_rate_commitment_years=-1,
            interest_rate_per_year_percent=5,
            loan_amount=100000,
            purchasing_price=-1,
            repayment_rate_percent=None,
        )
        assert credit.get_yearly_rate() == pytest.approx(23097.48, 0.01)
