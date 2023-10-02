import numpy_financial as npf

class FixedMortgageProduct():
    def __init__(self,**kwargs):
        if 'pv' in kwargs: self.set_pv(kwargs['pv'])
        if 'nper' in kwargs: self.set_nper(kwargs['nper'])
        if 'rate' in kwargs: self.set_rate(kwargs['rate'])
        if 'pmt'  in kwargs: self.set_pmt(kwargs['pmt'])

    def set_pv(self, value=None):
        if value is None:
            value = npf.pv(self._rate/12, self._nper*12, -self._pmt)
        self._pv = value

    def get_pv(self):
        self.set_pv()
        return self._pv
    
    def set_nper(self, value=None):
        if value is None:
            value = npf.nper(self._rate/12, -self._pmt, self._pv)/12
        self._nper = value

    def get_nper(self):
        self.set_nper()
        return self._nper

    def set_rate(self, value=None):
        if value is None:
            value = npf.rate(self._nper*12, -self._pmt, self._pv)*12
        self._rate = value

    def get_rate(self):
        self.set_rate()
        return self._rate/12
    
    def set_pmt(self, value=None):
        if value is None:
            value = -npf.pmt(self._rate/12, self._nper*12, self._pv)
        self._pmt = value

    def get_pmt(self):
        self.set_pmt()
        return self._pmt
