# Digital Twin for Infection Risk Modelling in Lifts

This project presents a real-time Digital Twin system designed to assess and manage airborne infection risk in elevator environments using ambient sensor data and predictive modelling.

## Project Summary

Elevators are high-risk zones for disease transmission due to limited ventilation and short but dense occupancy periods. This Digital Twin integrates environmental sensors, machine learning, and epidemiological models to simulate and forecast infection risk for diseases like COVID-19, tuberculosis, and measles.

## Key Features

- **Real-Time Sensor Integration**: Captures CO₂ concentration, temperature, humidity, and occupancy using low-cost hardware (e.g., MH-Z19C, DHT22).
- **Wells-Riley Modelling**: Calculates disease-specific airborne transmission probabilities.
- **CO₂ Forecasting**: Implements LSTM and Random Forest models to predict ventilation trends.
- **Environmental Comfort Modelling**: Assesses air quality based on ASHRAE standards.
- **Anomaly Detection**: Identifies unusual spikes in CO₂ or sensor faults using Isolation Forest.
- **Risk Classification**: Classifies zones as Safe / Moderate / High using Decision Trees.
- **Visualization**: Real-time dashboards with ventilation curves, comfort zones, and risk trends.

## Tech Stack

- **Language**: Python
- **Libraries**: pandas, scikit-learn, keras, matplotlib, seaborn, numpy
- **Hardware**: Raspberry Pi Pico W, MH-Z19C, DHT22
- **Cloud**: Google Sheets (for live data sync)
- **Version Control**: Git, GitHub, GitLab

## Folder Structure
 - FYP_Models/ - These contain the data analyze on the data collected from the elevator. 
 - Picow_files/ - They contain the files which were uploaded to Raspberry Pi Pico W. 
 - Tableau/ - This folder contains the visualization for the data collected. 
 - app.py - It is a Flask App which transfers data from Pico W to Google Sheets. 


## Sample Output

- Infection Probability (COVID-19): ~2.3%
- Measles Risk in Poor Ventilation: ~32%
- >80% time outside ASHRAE comfort zone in some lifts

## Use Cases

- Real-time risk tracking for university dorm lifts
- Building management system integration
- Public health simulation for policy recommendations

## Getting Started

1. Clone the repo:
   git clone https://gitlab.ntulily.org/anouskha005/digital-twins.git
   pip install -r requirements.txt
