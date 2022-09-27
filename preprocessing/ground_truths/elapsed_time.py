import os
import pickle
from datetime import datetime, timedelta
from tqdm import tqdm


def get_elapsed_times(file_buffer):
    registration_start = []
    registration_end = []
    seizure_start = []
    seizure_end = []
    registration_elapsed_time = []
    seizure_elapsed_time = []

    registration_end_seconds = []
    seizure_start_seconds = []
    seizure_end_seconds = []

    for sentence in file_buffer:
        this_sentence = sentence
        if 'Registration' in this_sentence:
            timestamp_str = this_sentence.split(':')
            timestamp_str_list = timestamp_str[1][1:-1]
            if 'start' in this_sentence:
                registration_start.append(timestamp_str_list)
            elif 'end' in this_sentence:
                registration_end.append(timestamp_str_list)

        elif 'Seizure' in this_sentence:
            if 'start' in this_sentence:
                timestamp_str = this_sentence.split(':')
                timestamp_str_list = timestamp_str[1][1:-1]
                seizure_start.append(timestamp_str_list)
            elif 'end' in this_sentence:
                timestamp_str = this_sentence.split(':')
                timestamp_str_list = timestamp_str[1][1:-1]
                seizure_end.append(timestamp_str_list)


    for i in range(len(registration_start)):
        # Experiment beginning and ending
        exp_start_timestamp = registration_start[i]
        exp_end_timestamp = registration_end[i]

        exp_start_time, exp_end_time, exp_elapsed_time = calculate_elapsed_time(
            exp_start_timestamp,
            exp_end_timestamp)
        registration_start[i] = exp_start_time
        registration_end[i] = exp_end_time
        registration_elapsed_time.append(exp_elapsed_time)

        # Seizure beginning and ending
        seizure_start_timestamp = seizure_start[i]
        seizure_end_timestamp = seizure_end[i]

        sei_start_time, sei_end_time, sei_elapsed_time = calculate_elapsed_time(
            seizure_start_timestamp,
            seizure_end_timestamp)
        seizure_start[i] = sei_start_time
        seizure_end[i] = sei_end_time
        seizure_elapsed_time.append(sei_elapsed_time)

        # Experiment and seizure
        _, _, exp_ends_seconds = calculate_elapsed_time(
            exp_start_time,
            exp_end_time
        )

        _, _, seizure_starts_seconds = calculate_elapsed_time(
            exp_start_time,
            sei_start_time
        )

        _, _, seizure_ends_seconds = calculate_elapsed_time(
            sei_end_time,
            exp_end_time
        )
        registration_end_seconds.append(exp_ends_seconds)
        seizure_start_seconds.append(seizure_starts_seconds)
        seizure_end_seconds.append(seizure_ends_seconds)

    return (
        registration_start,
        registration_end,
        registration_elapsed_time,

        seizure_start,
        seizure_end,
        seizure_elapsed_time,

        registration_end_seconds,
        seizure_start_seconds,
        seizure_end_seconds
    )

def calculate_elapsed_time(start_timestamp, end_timestamp):
    if not isinstance(start_timestamp, str) and not isinstance(end_timestamp, str):
        start_time = start_timestamp
        end_time = end_timestamp

    elif int(start_timestamp.split('.')[0]) > int(end_timestamp.split('.')[0]):
        start_time = datetime(
            year=2021,
            month=12,
            day=11,
            hour=int(start_timestamp.split('.')[0]),
            minute=int(start_timestamp.split('.')[1]),
            second=int(start_timestamp.split('.')[2])
        )

        end_time = datetime(
            year=2021,
            month=12,
            day=12,
            hour=int(end_timestamp.split('.')[0]),
            minute=int(end_timestamp.split('.')[1]),
            second=int(end_timestamp.split('.')[2])
        )
    else:
        start_time = datetime(
            year=2021,
            month=12,
            day=11,
            hour=int(start_timestamp.split('.')[0]),
            minute=int(start_timestamp.split('.')[1]),
            second=int(start_timestamp.split('.')[2])
        )

        end_time = datetime(
            year=2021,
            month=12,
            day=11,
            hour=int(end_timestamp.split('.')[0]),
            minute=int(end_timestamp.split('.')[1]),
            second=int(end_timestamp.split('.')[2])
        )

    time_elapsed = end_time - start_time
    return start_time, end_time, time_elapsed.total_seconds()


if __name__ == "__main__":
    experiment_start = {}
    experiment_end = {}
    experiment_durations = {}

    seizure_start = {}
    seizure_end = {}
    seizure_durations = {}

    experiment_end_seconds = {}
    seizure_start_seconds = {}
    seizure_end_seconds = {}

    patient_dataset_path = r"D:/PacificAutism/github-code/data"
    for folder in tqdm(os.listdir(patient_dataset_path), desc="Processing the .txt file of each folder . . ."):
        patient_folder_path = os.path.join(patient_dataset_path, folder)
        for patient_file in os.listdir(patient_folder_path):
            if patient_file.split(".")[-1] == "txt":
                patient_txt_file = os.path.join(patient_folder_path, patient_file)
                f = open(patient_txt_file, "r")
                (
                    this_experiment_start,
                    this_experiment_end,
                    this_experiment_durations,

                    this_seizure_start,
                    this_seizure_end,
                    this_seizure_durations,

                    this_experiment_ends_seconds,
                    this_seizure_starts_seconds,
                    this_seizure_ends_seconds
                ) = get_elapsed_times(f)

                experiment_start[patient_file.split('.')[0]] = this_experiment_start
                experiment_end[patient_file.split('.')[0]] = this_experiment_end
                experiment_durations[patient_file.split('.')[0]] = this_experiment_durations

                seizure_start[patient_file.split('.')[0]] = this_seizure_start
                seizure_end[patient_file.split('.')[0]] = this_seizure_end
                seizure_durations[patient_file.split('.')[0]] = this_seizure_durations

                experiment_end_seconds[patient_file.split('.')[0]] = this_experiment_ends_seconds
                seizure_start_seconds[patient_file.split('.')[0]] = this_seizure_starts_seconds
                seizure_end_seconds[patient_file.split('.')[0]] = this_seizure_ends_seconds

    patient_dict_path = r"D:/PacificAutism/data/Patient_dict/"

    if not os.path.exists(patient_dict_path):
        os.mkdir(patient_dict_path)

    with open(os.path.join(patient_dict_path, 'experiment_start.pkl'), 'wb') as f:
        pickle.dump(experiment_start, f)
    with open(os.path.join(patient_dict_path, 'experiment_end.pkl'), 'wb') as f:
        pickle.dump(experiment_end, f)
    with open(os.path.join(patient_dict_path, 'experiment_duration.pkl'), 'wb') as f:
        pickle.dump(experiment_durations, f)

    with open(os.path.join(patient_dict_path, 'seizure_start.pkl'), 'wb') as f:
        pickle.dump(seizure_start, f)
    with open(os.path.join(patient_dict_path, 'seizure_end.pkl'), 'wb') as f:
        pickle.dump(seizure_end, f)
    with open(os.path.join(patient_dict_path, 'seizure_duration.pkl'), 'wb') as f:
        pickle.dump(seizure_durations, f)

    with open(os.path.join(patient_dict_path, 'experiment_end_seconds.pkl'), 'wb') as f:
        pickle.dump(experiment_end_seconds, f)
    with open(os.path.join(patient_dict_path, 'seizure_start_seconds.pkl'), 'wb') as f:
        pickle.dump(seizure_start_seconds, f)
    with open(os.path.join(patient_dict_path, 'seizure_end_seconds.pkl'), 'wb') as f:
        pickle.dump(seizure_end_seconds, f)