import CreditCard


class PredatoryCreditCard(CreditCard):
    """An extension to credit card that compounds interests and fees."""

    def __init__(self, customer, bank, acnt, limit, apr):
        """Create a new predatory card instance

        The initial balance is zero.

        customer    the name of the customer (e.g. 'John Bowman')
        bank        the anme of the bank (e.g. 'California Savings')
        acnt        the acount identifier (e.g. '5391 0375 9387 5309')
        limit       credit limit (measured in dollars)
        apr         annual percentage rate (e.g. 0.0825 for 8.25% APR)
        """

        success = super().charge(price)        # call inherited method
        if not success:
            self._balance += 5                    # access penalty
        return success                         # caller expects return value

    def process_month(self):
        """Assess monthly interest on outstanding balance."""
        if self._balance > 0:
            # if positive balance, converty APR to monthly multiplicative factor
            monthly_factor = pow(1+self._apr, 1/12)
            self._balance *= monthly_factor
