from HRinst import HRinst
import numpy as np

dataset = (np.arange(0, 29), np.array([0, 1, 7, 1, 0, -1, 10, 10, 3, 2, 0, 4,
                                       5, 0, 9, 10, 11, 10, 0, 1, 2, 4, 3, 8.5,
                                       8.6, 8, 1, 2, 3]))
result = HRinst(dataset, filt=False, peak_threshold=65)


def test_hrinst():
    assert type(result) == np.ndarray
    assert result.shape[0] == 29
    assert np.all((result == (np.array([0, 0, 0, 0, 0, 0, 0, 0, 12, 12, 12, 12,
                                        12, 12, 12, 12, 12, 20 / 3, 20 / 3,
                                        20 / 3, 20 / 3, 20 / 3, 20 / 3, 20 / 3,
                                        20 / 3, 7.5, 7.5, 7.5, 7.5]))))


test_hrinst()
