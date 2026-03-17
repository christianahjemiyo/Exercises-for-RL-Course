# Exercises for RL Course

This repository contains course support material for reinforcement learning, centered around an interactive Streamlit dashboard for repeated quiz practice.

The app is designed to help with a common RL study problem: many algorithms can sound similar until you compare when they update, what kind of action space they handle, and what learning style they use. The dashboard turns that into short, repeated practice with immediate feedback.

## Live App

You can use the deployed dashboard here:

[`https://exercises-for-rl-course-7m4ysvwnmdj6pdlmqoxs55.streamlit.app/`](https://exercises-for-rl-course-7m4ysvwnmdj6pdlmqoxs55.streamlit.app/)

## What the Dashboard Includes

- A 300-question RL quiz bank
- 50-question shuffled quiz sessions
- Immediate answer review after submission
- A study guide that summarizes how major RL algorithms differ
- Missed-question review for targeted practice

## Run Locally

```powershell
python -m pip install -r requirements.txt
streamlit run rl_dashboard_300_unique.py
```

Then open the local URL shown by Streamlit in your terminal.

## Main App File

The Streamlit app entrypoint is:

`rl_dashboard_300_unique.py`

## Deployment

This project is deployed with Streamlit Community Cloud from the `main` branch of this repository.
