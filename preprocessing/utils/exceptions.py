class StringTimestampFormat(Exception):
    """
    -> Usage: in function calculate_duration() from utils.py
    -> Purpose: to check if the timestamp string literal has 3 components,
    corresponding to hh, mm, and ss in the format "hh.mm.ss".
    """
    required_timestamp_format: str = "hh.mm.ss"

    def __init__(self, entered_timestamp: str = None, *args):
        super().__init__(args)
        self.entered_timestamp = entered_timestamp

    def __str__(self):
        exception_message = "The entered timestamp {} does not fit the " \
                            "required format of {}".format(self.entered_timestamp, self.required_timestamp_format)
        return exception_message


class ECGSignalIdentifier(Exception):

    def __init__(self, filename: str = None, ecg_signal_names: list = None, *args):
        super(ECGSignalIdentifier, self).__init__(args)
        self.filename = filename
        self.ecg_signal_names = ecg_signal_names

    def __str__(self):
        exception_message = "The file {} does not contain any ECG channels.Currently available ECG channels are {}." \
                            "Please edit /preprocessing/dataset_info.py to include an ECG channel if required."\
            .format(self.filename, self.ecg_signal_names)
        return exception_message
