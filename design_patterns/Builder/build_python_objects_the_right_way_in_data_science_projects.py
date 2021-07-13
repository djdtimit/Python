class Bond:
 start = None
 maturity = None
 coupon = None
 yield_rate = None
 notional = None
 holder = None
 issuer = None

class BondBuilder:
    def __init__(self, maturity, start, coupon, yield_rate, notional):
        #we can call a complex machine learning model or get data from 
        #external sources here too
        self._bond = Bond()
        self._bond.maturity = maturity
        self._bond.start = start
        self._bond.coupon = coupon
        self._bond.yield_rate = yield_rate
        self._bond.notional = notional
        return self

    def set_holder(self, holder):
        #   this can call a machine learning model if required
        self._bond.holder = holder
        return self

    def set_issuer(self, issuer):
        # Again, this can call a complex machine learning model
        self._bond.issuer = issuer
        return self

    def build():
        if self._bond is None:
            raise ValueError('Bond is empty. Please build properly')
        return self._bond

if __name__ == "__main__":
    bond = BondBuilder(maturity, start, coupon, yield_rate, notional).build()

    bond = BondBuilder(maturity, start, coupon, yield_rate, notional).set_issuer(issuer).build()

    bond = BondBuilder(maturity, start, coupon, yield_rate, notional).set_issuer(issuer).set_holder(holder).build() 