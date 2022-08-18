import os
import pyedflib
import h5py
from typing import Union
from tqdm import tqdm
from preprocessing.core.preprocess_template import PreprocessTemplate
from preprocessing.dataset_info import dataset1_ecg_variables
from preprocessing.utils.exceptions import ECGSignalIdentifier


class EDFFiles(PreprocessTemplate):

    def __init__(self):
        self._channels = None
        self._filepath = None
        self._data = None
        self._ecg_data = None
        self._info = None

    def read_data(self, filepath: Union[str, os.PathLike]) -> None:
        self._filepath = filepath
        self._data = pyedflib.EdfReader(filepath)

        """
        Depending on the file selected, the number of channels and the name of the channel containing ECG 
        data may differ, please refer to /preprocessing/file_types/edf_files_readme.md for more information
        on this dataset.
        """

    def process_data(self) -> None:
        print("\n Number of signals = {}".format(self._data.signals_in_file))
        self._channels = self._data.getSignalLabels()

        ecg_channel_idx = []  # This is a list because some files have multiple ECG channels, for example, [ECG1, ECG2]

        for ecg_signal_name in dataset1_ecg_variables:
            if ecg_signal_name in self._channels:
                ecg_channel_idx.append(self._channels.index(ecg_signal_name))

        if len(ecg_channel_idx) == 0:
            raise ECGSignalIdentifier(filename=self._filepath, ecg_signal_names=dataset1_ecg_variables)
        else:
            print("ECG data is in these indices: {}".format(ecg_channel_idx))
            print("\n ECG data is = ")
            for ecg_idx in ecg_channel_idx:
                seconds = self._data.readSignal(ecg_idx).shape[0]/512
                minutes = seconds/60
                hours = minutes/60
                print("\nECG datapoints={}"
                      "\nSeconds = {}"
                      "\n Minutes = {}"
                      "\n Hours = {}".format(self._data.readSignal(ecg_idx).shape[0], seconds, minutes, hours))
                print("\n")

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