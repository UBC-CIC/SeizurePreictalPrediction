import os
import pyedflib
import h5py
from typing import Union
from tqdm import tqdm
from preprocessing.core.preprocess_template import PreprocessTemplate


class EDFFiles(PreprocessTemplate):

    def __init__(self):
        self._filepath = None
        self._data = None
        self._ecg_data = None
        self._info = None

    def read_data(self, filepath: Union[str, os.PathLike]) -> None:
        self._filepath = filepath
        self._data = pyedflib.EdfReader(filepath)

        """
        There are 33 channels:
        [0]: 'EEG Fp1'  [1]: 'EEG F3'   [2]: 'EEG C3'   [3]: 'EEG P3'
        [4]: 'EEG O1'   [5]: 'EEG F7'   [6]: 'EEG T3'   [7]: 'EEG T5'
        [8]: 'EEG Fc1'  [9]: 'EEG Fc5'  [10]: 'EEG Cp1' [11]: 'EEG Cp5'
        [12]: 'EEG F9'  [13]: 'EEG Fz'  [14]: 'EEG Cz'  [15]: 'EEG Pz'
        [16]: 'EEG Fp2' [17]: 'EEG F4'  [18]: 'EEG C4'  [19]: 'EEG P4'
        [20]: 'EEG O2'  [21]: 'EEG F8'  [22]: 'EEG T4'  [23]: 'EEG T6'
        [24]: 'EEG Fc2' [25]: 'EEG Fc6' [26]: 'EEG Cp2' [27]: 'EEG Cp6'
        [28]: 'EEG F10' [29]: 'EKG EKG' [30]: 'SPO2'    [31]: 'HR'
        [32]: 'MK'

        
        """

    def process_data(self) -> None:
        print("\n Number of signals = {}".format(self._data.signals_in_file))
        print("\n Channels = {}".format(self._data.getSignalLabels()))

        # ecg_index = channels.index('EKG EKG')
        # self._ecg_data = raw_data[ecg_index]

    def store_data(self, destination_dir: Union[str, os.PathLike]):
        if not os.path.exists(destination_dir):
            os.mkdir(destination_dir)
        filepath = os.path.join(destination_dir, self._filepath.split(os.sep)[-1].split('.')[0]+'.hdf5')
        hdf5_file = h5py.File(filepath, 'w')
        hdf5_file.create_dataset('ecg', data=self._ecg_data)
        hdf5_file.close()

    def run_pipeline(self, edf_directory: Union[str, os.PathLike], destination_directory: Union[str, os.PathLike]):
        for patient_folder in tqdm(os.listdir(edf_directory), desc="Processing and storing each the .edf file(s) for "
                                                                   "each patient. . ."):
            for file in os.listdir(os.path.join(edf_directory, patient_folder)):
                if file.split('.')[-1] == "edf":
                    print("\n\n File = {}".format(file))
                    this_filepath = os.path.join(edf_directory, patient_folder, file)
                    self.read_data(filepath=this_filepath)
                    self.process_data()
                    # self.store_data(destination_dir=destination_directory)


if __name__ == "__main__":
    thisobj = EDFFiles()
    thisobj.run_pipeline(
        edf_directory=r'D:\PacificAutism\github-code\data',
        destination_directory=r'D:\PacificAutism\data\script_check'
    )
