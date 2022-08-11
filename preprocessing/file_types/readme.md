# Dataset 1 - Billeci et al, 2018

## Overview
This dataset contains ECG/EKG (electrocardiogram) and EEG (electroencephalogram) signals aquired in patients who have epilepsy. The ECG was measured with a sampling rate of 512 Hz. The signals analyzed in this study were acquired prospectively or retrospectively from patients admitted to Unit of Neurology and Neurophysiology, Department of Neurological and Neurosensorial Sciences, University of Siena, Italy. The study was approved by the Ethical Committee of the University of Siena and performed in accordance with the Declaration of Helsinki. At the time of admission at the clinics, each patient signed a written informed consent in which agrees to the video registration and to the use of the data for a possible scientific divulgation (Billeci et al, 2018).

## Components
1. Text or txt files: Contains information about the data acquisition i.e. registration start and end times (hh.mm.ss), seizure start and end times (hh.mm.ss), and the electrodes involved at the seizure onset.
2. European Data Format (EDF) files: For storing medical time series information.

## Overview of the EDF files:
- Channels: EDF files may contain anywhere between 33 - 129 signals.

| Patient      | Number of channels | Channel containing ECG data |
| ------------ | ------------------ | --------------------------- |
| Patient01   | 33  | 'EKG EKG'      |
| Patient02   | 129 | 'ECG1', 'ECG2' |
| Patient03   | 129 | 'ECG1', 'ECG2' |
| Patient04   | 35  | 'EKG EKG'      |
| Patient05   | 45  | 'EKG EKG'      |
| Patient06   | 45  | 'EKG EKG'      |
| Patient07   | 129 | 'ECG1', 'ECG2' |
| Patient08 - seizure 1   | 37  | 'EKG EKG'      |
| Patient08 - seizure 2   | 37  | 'EKG EKG'      |
| Patient08 - seizure 3   | 37  | 'EKG EKG'      |
| Patient09 - seizure 1  | 37  | 'EKG EKG'      |
| Patient09 - seizure 2  | 37  | 'EKG EKG'      |
| Patient09 - seizure 3  | 37  | 'EKG EKG'      |
| Patient09 - seizure 4  | 37  | 'EKG EKG'      |
| Patient09 - seizure 5  | 37  | 'EKG EKG'      |
| Patient10 - seizure 1  | 45  | 'EKG EKG'      |
| Patient10 - seizure 2  | 45  | 'EKG EKG'      |
| Patient11 - seizure 1  | 45  | 'EKG EKG'      |
| Patient11 - seizure 2  | 45  | 'EKG EKG'      |
| Patient11 - seizure 3  | 45  | 'EKG EKG'      |
| Patient11 - seizure 456| 45  | 'EKG EKG'      |
| Patient11 - seizure 789| 45  | 'EKG EKG'      |
| Patient11 - seizure 10 | 45  | 'EKG EKG'      |
| Patient12 - seizure 1  | 45  | 'EKG EKG'      |
| Patient12 - seizure 2  | 45  | 'EKG EKG'      |
| Patient12 - seizure 3  | 45  | 'EKG EKG'      |
| Patient13 - seizure 1  | 45  | 'EKG EKG'      |
| Patient13 - seizure 2  | 45  | 'EKG EKG'      |
| Patient13 - seizure 3  | 45  | 'EKG EKG'      |
| Patient14 - seizure 1  | 49  | ECG Unavailable|
| Patient14 - seizure 2  | 49  | ECG Unavailable|
| Patient14 - seizure 3  | 49  | ECG Unavailable|
| Patient15 - seizure 1  | 49  | ECG Unavailable|
| Patient15 - seizure 2  | 49  | ECG Unavailable|

- Channel names type 1 (33 signals): For example, ['EEG Fp1', 'EEG F3', 'EEG C3', 'EEG P3', 'EEG O1', 'EEG F7', 'EEG T3', 'EEG T5', 'EEG Fc1', 'EEG Fc5', 'EEG Cp1', 'EEG Cp5', 'EEG F9', 'EEG Fz', 'EEG Cz', 'EEG Pz', 'EEG Fp2', 'EEG F4', 'EEG C4', 'EEG P4', 'EEG O2', 'EEG F8', 'EEG T4', 'EEG T6', 'EEG Fc2', 'EEG Fc6', 'EEG Cp2', 'EEG Cp6', 'EEG F10', 'EKG EKG', 'SPO2', 'HR', 'MK']
    - Channel name descriptions (For more information on these, [click here](https://en.wikipedia.org/wiki/10%E2%80%9320_system_(EEG)#Electrode_labeling)):
        - EEG electrodes [^1] 
        [^1]: Even numbered electrodes are placed on the right side of the head, odd numbered electrodes are placed on the left side. This system applies to the collection of EOG (measurement of eyes), EMG (measurement of skeletal muscles), and ECG (measurement of heart) data as well.

            - EEG Fpx: Pre-fontal electrodes
            - EEG Fx: Frontal electrodes
            - EEG Fcx: Unknown
            - EEG Cx: Central electrodes
            - EEG Cpx: Unknown
            - EEG Px: Parietal electrodes
            - EEG Tx: Temporal electrodes
            - EEG Fz, Pz, Cz,: Ground/reference/"zero" electrodes
        - Others:
            - EKG/ECG: Electric signal from the heart
            - SPO2: Blood oxygen
            - HR: Heart rate (Note: For some patients this was probably not monitored. For example, for Patient 1, this returns an array of 8e-06 i.e. a constant low electrical signal)
            - MK: Unknown
            - EEG Fz, Pz, Cz,: Ground/reference/"zero" electrodes

- Channel names type 2 (129) signals: For example, ['Event', 'Fp1', 'Fp2', 'F3', 'F4', 'C3', 'C4', 'P3', 'P4', 'O1', 'O2', 'F7', 'F8', 'T3', 'T4', 'T5', 'T6', 'Fz', 'Cz', 'Pz', 'Fpz', 'Fc1', 'Fc2', 'Fc5', 'Fc6', 'Cp1', 'Cp2', 'Cp5', 'Cp6', 'F9', 'F10', 'ECG1', 'ECG2', 'C33', 'C34', 'C35', 'C36', 'C37', 'C38', 'C39', 'C40', 'C41', 'C42', 'C43', 'C44', 'C45', 'C46', 'C47', 'C48', 'C49', 'C50', 'C51', 'C52', 'C53', 'C54', 'C55', 'C56', 'C57', 'C58', 'C59', 'C60', 'C61', 'C62', 'C63', 'C64', 'C65', 'C66', 'C67', 'C68', 'C69', 'C70', 'C71', 'C72', 'C73', 'C74', 'C75', 'C76', 'C77', 'C78', 'C79', 'C80', 'C81', 'C82', 'C83', 'C84', 'C85', 'C86', 'C87', 'C88', 'C89', 'C90', 'C91', 'C92', 'C93', 'C94', 'C95', 'C96', 'C97', 'C98', 'C99', 'C100', 'C101', 'C102', 'C103', 'C104', 'C105', 'C106', 'C107', 'C108', 'C109', 'C110', 'C111', 'C112', 'C113', 'C114', 'C115', 'C116', 'C117', 'C118', 'C119', 'C120', 'C121', 'C122', 'C123', 'C124', 'C125', 'C126', 'C127', 'C128']
    - Channel name descriptions:
        - EEG electrodes [^1] 
        [^1]: Even numbered electrodes are placed on the right side of the head, odd numbered electrodes are placed on the left side. This system applies to the collection of EOG (measurement of eyes), EMG (measurement of skeletal muscles), and ECG (measurement of heart) data as well.

            - Fpx: Pre-fontal electrodes
            - Fx: Frontal electrodes
            - Ox: Occipital electrodes
            - Tx: Temporal electrodes
            - Px: Parietal electrodes

        - Others:
            - EKG/ECG: Electric signal from the heart
            - SPO2: Blood oxygen
            - HR: Heart rate (Note: For some patients this was probably not monitored. For example, for Patient 1, this returns an array of 8e-06 i.e. a constant low electrical signal)
            - MK: Unknown

# References
- Billeci, L., Marino, D., Insana, L., Vatti, G., & Varanini, M. (2018). Patient-specific seizure prediction based on heart rate variability and recurrence quantification analysis. PloS one, 13(9), e0204339.