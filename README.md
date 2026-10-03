# EOG-Based Real-Time Eye Tracking

A real-time eye-tracking system using **Electrooculography (EOG)** signals and machine learning to classify **horizontal eye movement, vertical eye movement, and blinking**.

The system collects EOG data through a microcontroller, prepares and labels the collected data, trains three **Random Forest** classifiers, and performs real-time eye-movement prediction using Python.

> **Project Type:** Embedded Systems + Biomedical Signal Processing + Machine Learning
> **Core Methods:** EOG signal acquisition, dataset preparation, Random Forest classification, real-time inference

---

## 1. Project Overview

Eye movement produces measurable electrical potential changes around the eyes. These signals can be captured using EOG sensing and processed to determine the direction of eye movement.

This project develops a real-time eye-tracking pipeline that classifies three categories of eye activity:

* **Horizontal movement:** Left, no horizontal movement, right
* **Vertical movement:** Down, no vertical movement, up
* **Blink detection:** No blink or blink

Instead of using a single model for every task, the system uses **three separate Random Forest classifiers**, one for each classification problem.

---

## 2. System Architecture

```text
                EOG Sensors
                     │
                     ↓
             Microcontroller
                     │
                     ↓
              Data Collection
                     │
                     ↓
            Raw EOG Measurements
                     │
                     ↓
              Data Labeling
                     │
          ┌──────────┼──────────┐
          ↓          ↓          ↓
      Horizontal   Vertical   Blink
       Dataset     Dataset    Dataset
          │          │          │
          └──────────┼──────────┘
                     ↓
          Random Forest Training
                     │
          ┌──────────┼──────────┐
          ↓          ↓          ↓
     Horizontal   Vertical   Blink
      Classifier  Classifier Classifier
          │          │          │
          └──────────┼──────────┘
                     ↓
           Real-Time Inference
                     │
                     ↓
          Final Prediction Stage
                     │
                     ↓
      Eye Movement / Blink Output
```

---

## 3. Main Objectives

The project focuses on building a complete sensing-to-prediction pipeline:

1. Acquire EOG measurements using a microcontroller.
2. Collect data for different eye movements.
3. Label the collected measurements.
4. Prepare separate datasets for horizontal movement, vertical movement, and blinking.
5. Train three Random Forest classification models.
6. Perform real-time inference on incoming EOG data.
7. Process the predictions through a final prediction stage for improved output stability.

---

## 4. Eye-Movement Classification

### Horizontal Eye Movement

The horizontal classifier uses three classes:

| Label | Meaning                |
| ----: | ---------------------- |
|   `0` | Leftward eye movement  |
|   `1` | No horizontal movement |
|   `2` | Rightward eye movement |

### Vertical Eye Movement

The vertical classifier uses three classes:

| Label | Meaning               |
| ----: | --------------------- |
|   `0` | Downward eye movement |
|   `1` | No vertical movement  |
|   `2` | Upward eye movement   |

### Blink Detection

The blink classifier uses two classes:

| Label | Meaning  |
| ----: | -------- |
|   `0` | No blink |
|   `1` | Blink    |

These class definitions follow the original project structure.

---

## 5. Data Acquisition

EOG measurements are collected from the sensing hardware through a microcontroller.

The acquisition stage converts the physical eye-movement activity into data that can be stored and processed for machine-learning model development.

### Data Flow

```text
Eye Movement
     ↓
EOG Signal
     ↓
Sensor Acquisition
     ↓
Microcontroller
     ↓
Collected Data
     ↓
Dataset Preparation
```

The original project uses a Python data-collection script to transfer the EOG measurements into a spreadsheet-based dataset.

---

## 6. Dataset Preparation

The collected data is divided into three application-specific datasets.

```text
horizontal_eye_movement_data/
vertical_eye_movement_data/
blink_data/
```

Each dataset corresponds to one classification task.

The data-processing workflow is:

```text
Raw EOG Data
     ↓
Label Samples
     ↓
Organize by Task
     ↓
Training Dataset
```

---

## 7. Machine Learning

The project uses **three Random Forest classifiers**:

```text
                EOG Data
                   │
        ┌──────────┼──────────┐
        ↓          ↓          ↓
   Horizontal   Vertical    Blink
   Classifier   Classifier  Classifier
        ↓          ↓          ↓
     Left/None/   Down/None/  No Blink/
       Right        Up         Blink
```

Using separate models allows each classifier to specialize in a different prediction task.

The training notebook processes the labeled datasets and trains the three Random Forest models.

---

## 8. Real-Time Inference

After training, the system can process incoming EOG data in real time.

The inference pipeline is:

```text
Live EOG Data
     ↓
Feature / Data Processing
     ↓
Horizontal Model ──→ Horizontal Prediction
     ↓
Vertical Model   ──→ Vertical Prediction
     ↓
Blink Model      ──→ Blink Prediction
     ↓
Final Prediction Processing
     ↓
Terminal Output
```

The real-time inference stage generates predictions continuously from incoming data.

---

## 9. Final Prediction Stage

A separate processing stage is used after the initial real-time inference.

Its purpose is to process the immediate predictions and produce the final eye-movement output used by the system.

```text
Raw Model Predictions
          ↓
Prediction Processing
          ↓
Final Eye-Movement Decision
          ↓
Terminal Output
```

The original project describes this stage as a way to obtain a higher-accuracy final prediction from the real-time outputs.

---

## 10. Repository Structure

The original project files can be renamed to the following cleaner structure:

```text
EOG-Based-Real-Time-Eye-Tracking/
│
├── README.md
│
├── horizontal_eye_movement_data/
├── vertical_eye_movement_data/
├── blink_data/
│
├── collect_eog_data.py
├── label_eog_dataset.ipynb
├── train_eye_movement_models.ipynb
├── realtime_eog_inference.py
└── final_eye_movement_prediction.py
```

### File Mapping

| Name                               | Purpose                                              |
| ---------------------------------- | ---------------------------------------------------- |
| `horizontal_eye_movement_data`     | Horizontal movement training data                    |
| `vertical_eye_movement_data`       | Vertical movement training data                      |
| `blink_data`                       | Blink classification data                            |
| `collect_eog_data.py`              | Collect EOG measurements through the microcontroller |
| `label_eog_dataset.ipynb`          | Label collected samples                              |
| `train_eye_movement_models.ipynb`  | Train the three Random Forest models                 |
| `realtime_eog_inference.py`        | Perform real-time model inference                    |
| `final_eye_movement_prediction.py` | Process predictions and generate final output        |

---

## 11. Technologies and Concepts

### Hardware

* EOG sensing
* Microcontroller-based data acquisition

### Software

* Python
* Jupyter Notebook
* Machine Learning
* Random Forest classification

### Concepts

* Biomedical signal acquisition
* Data labeling
* Supervised learning
* Multiclass classification
* Binary classification
* Real-time inference
* Sensor-to-software data pipelines

---

## 12. Project Workflow

The complete workflow can be summarized as:

```text
1. Capture EOG signals
          ↓
2. Transfer and store measurements
          ↓
3. Label the collected samples
          ↓
4. Create task-specific datasets
          ↓
5. Train Random Forest classifiers
          ↓
6. Acquire live EOG measurements
          ↓
7. Run real-time classification
          ↓
8. Process predictions
          ↓
9. Produce final eye-movement output
```

---

## 13. What Makes the Project Interesting

The project combines multiple layers of engineering rather than relying on a single software algorithm.

```text
Physical Signal
      ↓
Sensor Acquisition
      ↓
Embedded Data Collection
      ↓
Dataset Engineering
      ↓
Machine Learning
      ↓
Real-Time Inference
```

This creates a complete pipeline from **biological signal acquisition to real-time machine-learning output**.

---

## 14. Applications

The eye-tracking concept can be used as a foundation for systems such as:

* Assistive human-machine interfaces
* Hands-free control systems
* Accessibility-oriented interfaces
* Eye-controlled devices
* Real-time biomedical signal interfaces
* Human-computer interaction systems

These are potential application areas of the underlying approach; this repository specifically demonstrates the eye-movement classification pipeline described above.

---

## 15. Key Learning Outcomes

Through this project, the following areas are covered:

* Understanding EOG-based signal acquisition
* Collecting sensor data through a microcontroller
* Building labeled machine-learning datasets
* Training multiple classification models
* Working with Random Forest algorithms
* Designing a real-time inference pipeline
* Processing model predictions for final output
* Connecting embedded data acquisition with Python-based ML

---

## 16. Project Highlights

**Signal Processing:** EOG-based eye-movement data acquisition

**Embedded Systems:** Microcontroller-based sensor data collection

**Machine Learning:** Three Random Forest classifiers

**Classification:** Horizontal movement, vertical movement, and blink detection

**Real-Time System:** Continuous prediction from incoming EOG measurements

**End-to-End Pipeline:** Sensor → dataset → training → inference → final prediction

---

## 18. Summary

The project demonstrates a complete **real-time EOG eye-tracking pipeline**.

EOG signals are acquired through a microcontroller, organized into task-specific datasets, and used to train three Random Forest classifiers for:

* Horizontal eye movement
* Vertical eye movement
* Blinking

The trained models are then used for real-time inference, followed by a final prediction-processing stage to generate the system output.

The project combines **embedded systems, biomedical signal acquisition, machine learning, and real-time Python processing** in one integrated application.
