from bradyTachyCardia import bradyTachyCardia as BTC
import numpy as np
def test_bradyTachyCardia():
    testerArray = np.array([100, 88, 101, 64, 160, 60, 59, 40, 71, 0, -1, 200, 90, 80, 62])
    BTClist = BTC(testerArray)
    assert len(BTClist) == np.size(testerArray)
    assert BTClist == ['T', 'N', 'T', 'N', 'T', 'B', 'B', 'B', 'N', 'B', 'B', 'T', 'N', 'N', 'N']