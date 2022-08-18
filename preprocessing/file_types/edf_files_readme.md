# Dataset 1 - Billeci et al, 2018

## Overview of the dataset
This dataset contains ECG/EKG (electrocardiogram) and EEG (electroencephalogram) signals aquired in patients who have epilepsy. The ECG was measured with a sampling rate of 512 Hz. The signals analyzed in this study were acquired prospectively or retrospectively from patients admitted to Unit of Neurology and Neurophysiology, Department of Neurological and Neurosensorial Sciences, University of Siena, Italy. The study was approved by the Ethical Committee of the University of Siena and performed in accordance with the Declaration of Helsinki. At the time of admission at the clinics, each patient signed a written informed consent in which agrees to the video registration and to the use of the data for a possible scientific divulgation (Billeci et al, 2018).

## Components
1. Text or txt files: Contains information about the data acquisition i.e. registration start and end times (hh.mm.ss), seizure start and end times (hh.mm.ss), and the electrodes involved at the seizure onset.
2. European Data Format (EDF) files: For storing medical time series information.

## Overview of the EDF files:
- Channels: EDF files may contain anywhere between 33 - 129 signals.

| Patient                 | Number of channels | Channel containing ECG data |
|-------------------------|--------------------|-----------------------------|
| Patient01               | 33                 | 'EKG EKG'                   |
| Patient02               | 129                | 'ECG1', 'ECG2'              |
| Patient03               | 129                | 'ECG1', 'ECG2'              |
| Patient04               | 35                 | 'EKG EKG'                   |
| Patient05               | 45                 | 'EKG EKG'                   |
| Patient06               | 45                 | 'EKG EKG'                   |
| Patient07               | 129                | 'ECG1', 'ECG2'              |
| Patient08 - seizure 1   | 37                 | 'EKG EKG'                   |
| Patient08 - seizure 2   | 37                 | 'EKG EKG'                   |
| Patient08 - seizure 3   | 37                 | 'EKG EKG'                   |
| Patient09 - seizure 1   | 37                 | 'EKG EKG'                   |
| Patient09 - seizure 2   | 37                 | 'EKG EKG'                   |
| Patient09 - seizure 3   | 37                 | 'EKG EKG'                   |
| Patient09 - seizure 4   | 37                 | 'EKG EKG'                   |
| Patient09 - seizure 5   | 37                 | 'EKG EKG'                   |
| Patient10 - seizure 1   | 45                 | 'EKG EKG'                   |
| Patient10 - seizure 2   | 45                 | 'EKG EKG'                   |
| Patient11 - seizure 1   | 45                 | 'EKG EKG'                   |
| Patient11 - seizure 2   | 45                 | 'EKG EKG'                   |
| Patient11 - seizure 3   | 45                 | 'EKG EKG'                   |
| Patient11 - seizure 456 | 45                 | 'EKG EKG'                   |
| Patient11 - seizure 789 | 45                 | 'EKG EKG'                   |
| Patient11 - seizure 10  | 45                 | 'EKG EKG'                   |
| Patient12 - seizure 1   | 45                 | 'EKG EKG'                   |
| Patient12 - seizure 2   | 45                 | 'EKG EKG'                   |
| Patient12 - seizure 3   | 45                 | 'EKG EKG'                   |
| Patient13 - seizure 1   | 45                 | 'EKG EKG'                   |
| Patient13 - seizure 2   | 45                 | 'EKG EKG'                   |
| Patient13 - seizure 3   | 45                 | 'EKG EKG'                   |
| Patient14 - seizure 1   | 49                 | ECG Unavailable             |
| Patient14 - seizure 2   | 49                 | ECG Unavailable             |
| Patient14 - seizure 3   | 49                 | ECG Unavailable             |
| Patient15 - seizure 1   | 49                 | ECG Unavailable             |
| Patient15 - seizure 2   | 49                 | ECG Unavailable             |

- **Channel names type 1 (33 signals):** For example, ['EEG Fp1', 'EEG F3', 'EEG C3', 'EEG P3', 'EEG O1', 'EEG F7', 'EEG T3', 'EEG T5', 'EEG Fc1', 'EEG Fc5', 'EEG Cp1', 'EEG Cp5', 'EEG F9', 'EEG Fz', 'EEG Cz', 'EEG Pz', 'EEG Fp2', 'EEG F4', 'EEG C4', 'EEG P4', 'EEG O2', 'EEG F8', 'EEG T4', 'EEG T6', 'EEG Fc2', 'EEG Fc6', 'EEG Cp2', 'EEG Cp6', 'EEG F10', 'EKG EKG', 'SPO2', 'HR', 'MK']
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


- **Channel names type 2 (35) signals:** For example, ['EEG Fp1', 'EEG F3', 'EEG C3', 'EEG P3', 'EEG O1', 'EEG F7', 'EEG T3', 'EEG T5', 'EEG Fc1', 'EEG Fc5', 'EEG Cp1', 'EEG Cp5', 'EEG F9', 'EEG Fz', 'EEG Cz', 'EEG Pz', 'EEG Fp2', 'EEG F4', 'EEG C4', 'EEG P4', 'EEG O2', 'EEG F8', 'EEG T4', 'EEG T6', 'EEG Fc2', 'EEG Fc6', 'EEG Cp2', 'EEG Cp6', 'EEG F10', 'EKG EKG', 'SPO2', 'HR', '1', '2', 'MK']
    - Channel name descriptions:
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
            - EEG Ox: Occipital electrodes

        - Others:
            - EKG EKG: Electric signal from the heart
            - SPO2: Blood oxygen
            - HR: Heart rate (Note: For some patients this was probably not monitored. For example, for Patient 1, this returns an array of 8e-06 i.e. a constant low electrical signal)
            - PLET: Pulse oximeter Plethysmograph
            - 1,2,61,62,63,64,B,C,D,MK: Unknown


-   **Channel names type 3 (37) signals:** For example, ['EEG Fp1', 'EEG F3', 'EEG C3', 'EEG P3', 'EEG O1', 'EEG F7', 'EEG T3', 'EEG T5', 'EEG Fc1', 'EEG Fc5', 'EEG Cp1', 'EEG Cp5', 'EEG F9', 'EEG Fz', 'EEG Cz', 'EEG Pz', 'EEG F4', 'EEG C4', 'EEG P4', 'EEG O2', 'EEG F8', 'EEG T4', 'EEG T6', 'EEG Fc2', 'EEG Fc6', 'EEG Cp2', 'EEG Cp6', 'EEG F10', 'EKG EKG', 'SPO2', 'HR', '1', '2', 'EEG FP2', 'EEG P9', 'EEG P10', 'B', 'C', 'D', 'PLET', '61', '62', '63', '64', 'MK']
    - Channel name descriptions:
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
            - EEG Ox: Occipital electrodes

        - Others:
            - EKG EKG: Electric signal from the heart
            - SPO2: Blood oxygen
            - HR: Heart rate (Note: For some patients this was probably not monitored. For example, for Patient 1, this returns an array of 8e-06 i.e. a constant low electrical signal)
            - 1,2,MK: Unknown


-   **Channel names type 4 (45) signals:** For example, ['EEG Fp1', 'EEG F3', 'EEG C3', 'EEG P3', 'EEG O1', 'EEG F7', 'EEG T3', 'EEG T5', 'EEG Fc1', 'EEG Fc5', 'EEG Cp1', 'EEG Cp5', 'EEG F9', 'EEG Fz', 'EEG Cz', 'EEG Pz', 'EEG F4', 'EEG C4', 'EEG P4', 'EEG O2', 'EEG F8', 'EEG T4', 'EEG T6', 'EEG Fc2', 'EEG Fc6', 'EEG Cp2', 'EEG Cp6', 'EEG F10', 'EKG EKG', 'SPO2', 'HR', '1', '2', 'EEG FP2', 'EEG P9', 'EEG P10', 'B', 'C', 'D', 'PLET', '61', '62', '63', '64', 'MK']
    - Channel name descriptions:
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
            - EEG Ox: Occipital electrodes

        - Others:
            - EKG EKG: Electric signal from the heart
            - SPO2: Blood oxygen
            - HR: Heart rate (Note: For some patients this was probably not monitored. For example, for Patient 1, this returns an array of 8e-06 i.e. a constant low electrical signal)
            - PLET: Pulse oximeter Plethysmograph
            - 1,2,61,62,63,64,B,C,D,MK: Unknown


-   **Channel names type 5 (49) signals:** For example, ['EEG Fp1', 'EEG F3', 'EEG C3', 'EEG P3', 'EEG O1', 'EEG F7', 'EEG T5', 'EEG Fc1', 'EEG Fc5', 'EEG Cp1', 'EEG Cp5', 'EEG F9', 'EEG Fz', 'EEG Pz', 'EEG F4', 'EEG C4', 'EEG P4', 'EEG O2', 'EEG F8', 'EEG T4', 'EEG T6', 'EEG Fc2', 'EEG Fc6', 'EEG Cp2', 'EEG Cp6', 'EEG F10', 'SPO2', 'HR', '1', '2', 'EEG FP2', 'EEG P9', 'EEG P10', 'PLET', '61', '62', '63', '64', 'EEG T3', 'EEG CZ', '3', '23', '33', '31', 'A', 'B', 'C', 'D', 'MK']
    - Channel name descriptions:
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
            - EEG Ox: Occipital electrodes

        - Others:
            - EKG EKG: Electric signal from the heart
            - SPO2: Blood oxygen
            - HR: Heart rate (Note: For some patients this was probably not monitored. For example, for Patient 1, this returns an array of 8e-06 i.e. a constant low electrical signal)
            - EEG Cz,: Ground/reference/"zero" electrodes
            - PLET: Pulse oximeter Plethysmograph
            - 1,2,3,23,31,33,A,B,C,D,61,62,63,64,MK: Unknown


- **Channel names type 6 (129) signals:** For example, ['Event', 'Fp1', 'Fp2', 'F3', 'F4', 'C3', 'C4', 'P3', 'P4', 'O1', 'O2', 'F7', 'F8', 'T3', 'T4', 'T5', 'T6', 'Fz', 'Cz', 'Pz', 'Fpz', 'Fc1', 'Fc2', 'Fc5', 'Fc6', 'Cp1', 'Cp2', 'Cp5', 'Cp6', 'F9', 'F10', 'ECG1', 'ECG2', 'C33', 'C34', 'C35', 'C36', 'C37', 'C38', 'C39', 'C40', 'C41', 'C42', 'C43', 'C44', 'C45', 'C46', 'C47', 'C48', 'C49', 'C50', 'C51', 'C52', 'C53', 'C54', 'C55', 'C56', 'C57', 'C58', 'C59', 'C60', 'C61', 'C62', 'C63', 'C64', 'C65', 'C66', 'C67', 'C68', 'C69', 'C70', 'C71', 'C72', 'C73', 'C74', 'C75', 'C76', 'C77', 'C78', 'C79', 'C80', 'C81', 'C82', 'C83', 'C84', 'C85', 'C86', 'C87', 'C88', 'C89', 'C90', 'C91', 'C92', 'C93', 'C94', 'C95', 'C96', 'C97', 'C98', 'C99', 'C100', 'C101', 'C102', 'C103', 'C104', 'C105', 'C106', 'C107', 'C108', 'C109', 'C110', 'C111', 'C112', 'C113', 'C114', 'C115', 'C116', 'C117', 'C118', 'C119', 'C120', 'C121', 'C122', 'C123', 'C124', 'C125', 'C126', 'C127', 'C128']
    - Channel name descriptions:
        - EEG electrodes [^1] 
        [^1]: Even numbered electrodes are placed on the right side of the head, odd numbered electrodes are placed on the left side. This system applies to the collection of EOG (measurement of eyes), EMG (measurement of skeletal muscles), and ECG (measurement of heart) data as well.

            - Fpx: Pre-fontal electrodes
            - Fx: Frontal electrodes
            - Ox: Occipital electrodes
            - Tx: Temporal electrodes
            - Px: Parietal electrodes

        - Others:
            - ECG1, ECG2: Electric signal from the heart
            - SPO2: Blood oxygen
            - HR: Heart rate (Note: For some patients this was probably not monitored. For example, for Patient 1, this returns an array of 8e-06 i.e. a constant low electrical signal)
            - MK: Unknown

# Details about the ECG data

| Number | Patient                   | Number of ECG datapoints (512 Hz/second) | Duration of ECG data (seconds//minutes//hours) |
|--------|---------------------------|------------------------------------------|------------------------------------------------|
| 1      | Patient01                 | 4460800                                  | 8712.5//145.21//2.42                           |
| 2      | Patient02 (ECG1 and ECG2) | 13800192                                 | 26953.5//449.225//7.49                         |
| 3      | Patient03 (ECG1 and ECG2) | 16646910                                 | 32513.50//541.90//9.03                         |
| 4      | Patient04                 | 24861184                                 | 48557.0//809.28//13.49                         |
| 5      | Patient05                 | 16101376                                 | 31448.0//524.13//8.74                          |
| 6      | Patient06                 | 4442624                                  | 8677.0//144.62//2.41                           |
| 7      | Patient07 (ECG1 and ECG2) | 11031062                                 | 21545.0//359.08//5.98                          |
| 8      | Patient08 Seizure 1       | 4733440                                  | 9245.0//154.08//2.57                           |
| 9      | Patient08 Seizure 2       | 3867648                                  | 7554.0//125.9//2.10                            |
| 10     | Patient08 Seizure 3       | 2523136                                  | 4928.0//82.13//1.37                            |
| 11     | Patient09 Seizure 1       | 4922880                                  | 9615.0//160.25//2.67                           |
| 12     | Patient09 Seizure 2       | 6461440                                  | 12620.0//210.33//3.51                          |
| 13     | Patient09 Seizure 3       | 4188160                                  | 8180.0//136.33//2.27                           |
| 14     | Patient09 Seizure 4       | 3596800                                  | 7025.0//117.08//1.95                           |
| 15     | Patient09 Seizure 5       | 3083264                                  | 6022.0//100.37//1.67                           |
| 16     | Patient10 Seizure 1       | 4215296                                  | 8233.0//137.22//2.29                           |
| 17     | Patient10 Seizure 2       | 4129280                                  | 8065.0//134.42//2.24                           |
| 18     | Patient11 Seizure 1       | 5110784                                  | 9982.0//166.37//2.77                           |
| 19     | Patient11 Seizure 10      | 4385280                                  | 8565.0//142.75//2.38                           |
| 20     | Patient11 Seizure 3       | 4461056                                  | 8713.0//145.22//2.42                           |
| 21     | Patient11 Seizure 456     | 8523776                                  | 16648.0//277.47//4.62                          |
| 22     | Patient11 Seizure 789     | 7656960                                  | 14955.0//249.25//4.15                          |
| 23     | Patient12 Seizure 1       | 5004288                                  | 9774.0//162.9//2.72                            |
| 24     | Patient12 Seizure 2       | 5004288                                  | 9774.0//162.9//2.72                            |
| 25     | Patient12 Seizure 3       | 1018368                                  | 1989.0//33.15//0.5525                          |
| 26     | Patient13 Seizure 1       | 4789760                                  | 9355.0//155.92//2.60                           |
| 27     | Patient13 Seizure 2       | 4767744                                  | 9312.0//155.2//2.59                            |
| 28     | Patient13 Seizure 3       | 6413824                                  | 12527.0//208.78//3.48                          |

# References
- Billeci, L., Marino, D., Insana, L., Vatti, G., & Varanini, M. (2018). Patient-specific seizure prediction based on heart rate variability and recurrence quantification analysis. PloS one, 13(9), e0204339.