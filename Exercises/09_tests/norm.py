import numpy as np


def normalize_array(arr: np.ndarray) -> np.ndarray:
    """Normalizes an array to the range [0, 1].
    The maximal element will be 1 and the minimal 0, while the
    scale remains the same.
    An array containing only identical values will be returned as a zeroed array.
    Paramaters
    ----------
    arr : np.ndarray
        Input array to normalize
    Returns
    -------
    np.ndarray
        Normalized array
    """
    arr = np.nan_to_num(arr)
    arr -= arr.min()
    max_ = arr.max()
    return arr if np.isclose(max_, 0.) else arr / max_

if __name__=='__main__':
    # mock data
    shape1 = (100, 100, 3)
    input1 = np.random.randint(20, 100, shape1)
    output1 = normalize_array(input1)

    shape2 = (10, 4, 1, 3)
    input2 = np.random.randn(*shape2) * 12
    output2 = normalize_array(input2)

    np.savez('snapshot_05_2020.npz', input1=input1, output1=output1, input2=input2, output2=output2)