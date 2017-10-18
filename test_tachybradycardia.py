def test_tachybradycardia():
    from tachybradycardia import bradycardia, tachycardia
    import numpy as np
    testerarray = np.array([100, 88, 101, 64, 160, 60, 59, 40, 71, 0, -1, 200,
                            90, 80, 62])
    bradylist = bradycardia(testerarray, 60)
    tachylist = tachycardia(testerarray, 100)
    assert len(bradylist) == np.size(testerarray)
    assert len(tachylist) == np.size(testerarray)
    assert bradylist == [0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0]
    assert tachylist == [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
