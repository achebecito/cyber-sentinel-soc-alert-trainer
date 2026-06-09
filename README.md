Cyber Sentinel: SOC Alert Trainer

Cyber Sentinel is a Python console-based cybersecurity training game where the user acts as a beginner SOC analyst. The player reviews simulated security alerts, classifies each alert by severity, and receives a final SOC Readiness Score with personalized recommendations.

Project Overview

The goal of this project is to help learners practice basic alert triage in a simple and interactive way. Instead of only answering isolated cybersecurity questions, the user must analyze short alert scenarios and decide whether each one is:

Benign
Suspicious
Critical

At the end of the training session, the program generates a performance report that shows the user's score, rank, strongest category, weakest category, and a recommended study path.

Why I Built This

Cybersecurity analysts often need to classify alerts quickly and accurately. This project was created as a small training simulator to practice that decision-making process.

The main idea is to transform a simple quiz into a basic SOC learning tool that gives feedback and helps the user understand where they need to improve.

Main Features
Simulated SOC alerts
Severity classification system
Input validation
Score tracking
Category-based performance analysis
SOC Readiness Score
Final training report
Personalized study recommendation
Alert Categories

The project includes alerts from different cybersecurity areas:

Phishing
Brute Force
Malware
Account Compromise
Data Loss
How It Works

The user reads each alert and chooses a severity level:

Benign
Suspicious
Critical

After each answer, the program explains whether the classification was correct and gives a short reason.

At the end, the program displays a report like this:

SOC TRAINING REPORT

Total alerts reviewed: 12
Correct classifications: 9
SOC Readiness Score: 75%
Rank: SOC Apprentice

Strongest area: Malware
Needs improvement: Phishing

Recommendation:
Review phishing indicators such as suspicious domains, urgency, credential requests, and unusual sender behavior.
Technologies Used
Python
Lists
Dictionaries
Loops
Conditional statements
Functions
Randomization
Console input and output
How to Run
Clone this repository:
git clone https://github.com/your-username/cyber-sentinel-soc-alert-trainer.git
Open the project folder:
cd cyber-sentinel-soc-alert-trainer
Run the program:
python main.py
Project Structure
cyber-sentinel-soc-alert-trainer/
│
├── main.py
└── README.md
Future Improvements

Possible future improvements include:

Adding more alert scenarios
Adding difficulty levels
Saving results to a file
Creating a graphical interface
Adding a timer for faster triage practice
Adding MITRE ATT&CK technique mapping
Adding a simulated SOC dashboard
