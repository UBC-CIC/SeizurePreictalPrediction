from preprocessing.file_types.edf_preprocess import EDFFiles
import numpy as np

if __name__ == "__main__":
    """
    thisobj = EDFFiles()
    thisobj.run_pipeline(
        edf_directory=r'D:\PacificAutism\github-code\data',
        destination_directory=r'D:\PacificAutism\data\script_check'
    )
    """
    path = r'D:\PacificAutism\data\script_check\Patient01.npy'
    with open(path, 'rb') as f:
        a = np.load(f, allow_pickle=True)
        print(a)
