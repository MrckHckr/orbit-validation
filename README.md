## Orbit Validation & Anomaly Detection

I developed an end-to-end pipeline that downloads real TLEs, propagates orbits with SGP4, compares the results with noisy observations, and uses LSTMs for anomaly detection, all automated with CI.

End-to-end aerospace data science project:
- Real TLE ingestion (Celestrak)
- Orbit propagation (SGP4)
- Validation vs observations
- LSTM-based anomaly detection
- CI pipeline with GitHub Actions

**Tech:** Python, Astropy, SGP4, TensorFlow, GitHub Actions
