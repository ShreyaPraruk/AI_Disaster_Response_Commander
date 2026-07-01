# 🚨 AI Disaster Response Commander

> An intelligent disaster response management system that helps emergency services quickly allocate ambulances, hospitals, and rescue teams during disasters using location-based decision making.

🌐 **Live Demo:** https://YOUR-RENDER-LINK.onrender.com

📂 **GitHub Repository:** https://github.com/ShreyaPraruk/AI_Disaster_Response_Commander

---

# 📖 Project Overview

AI Disaster Response Commander is a web-based application developed to improve emergency response during disasters. The system allows users to report disaster locations on an interactive map and automatically recommends the nearest available ambulance, hospital, and rescue resources.

The application also maintains incident history, displays live statistics, and provides an AI-based decision panel to assist emergency coordinators.

---

# ✨ Key Features

## 🌍 Interactive Disaster Map

- Report disasters by clicking directly on the map
- Supports multiple disaster types
  - 🔥 Fire
  - 🌊 Flood
  - 🌍 Earthquake

---

## 🤖 AI Decision Engine

The system automatically:

- Identifies the nearest available ambulance
- Finds the nearest hospital
- Calculates travel distance
- Estimates arrival time (ETA)
- Suggests the number of ambulances required
- Suggests the number of rescue teams required
- Displays disaster severity
- Displays AI confidence score
- Shows AI reasoning behind the decision

---

## 🚑 Emergency Resource Allocation

Resources are allocated based on:

- Disaster type
- Distance from incident
- Ambulance availability
- Hospital bed availability

---

## 📋 Incident History

Every reported disaster is automatically stored.

History includes:

- Incident ID
- Disaster Type
- Assigned Ambulance
- Assigned Hospital
- Estimated Arrival Time

---

## 📊 Live Dashboard

The dashboard displays:

- Total Incidents
- Total Fire Incidents
- Total Flood Incidents
- Total Earthquake Incidents

The statistics update automatically after every new disaster report.

---

## 💾 Database

SQLite is used to store:

- Disaster reports
- Ambulance allocation
- Hospital allocation
- ETA
- Distance
- Timestamp

---

# 🛠 Technology Stack

## Frontend

- HTML5
- CSS3
- JavaScript
- Leaflet.js
- Font Awesome

## Backend

- Python
- Flask

## Database

- SQLite

## Deployment

- GitHub
- Render

---

# 🏗 Project Architecture

```
User
   │
   ▼
Interactive Map
   │
   ▼
Flask API
   │
   ▼
AI Decision Engine
   │
   ├── Nearest Ambulance
   ├── Nearest Hospital
   ├── Resource Allocation
   ├── Severity Prediction
   └── ETA Calculation
   │
   ▼
SQLite Database
   │
   ▼
Dashboard + Incident History
```

---

# 📂 Project Structure

```
AI_Disaster_Response_Commander/

├── backend/
│   ├── app.py
│   ├── routes.py
│   ├── ai_engine.py
│   ├── database.py
│   └── disaster.db
│
├── frontend/
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   │
│   └── templates/
│       └── index.html
│
├── requirements.txt
├── README.md
└── render.yaml
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/ShreyaPraruk/AI_Disaster_Response_Commander.git
```

Go to the project folder

```bash
cd AI_Disaster_Response_Commander
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
cd backend

python app.py
```

Open

```
http://127.0.0.1:5000
```

---

# 📸 Screenshots 

### Dashboard Interactive Map

<img width="1894" height="951" alt="image" src="https://github.com/user-attachments/assets/8253c3c5-cc57-45f7-952a-63ab437aba0c" />

### AI Decision Panel

<img width="764" height="645" alt="image" src="https://github.com/user-attachments/assets/155c7ef3-59f8-412d-85f8-0164b3785a1a" />

### Incident History

<img width="1807" height="441" alt="image" src="https://github.com/user-attachments/assets/8801a070-a155-4b95-9e83-2d1535bce1b2" />
---

# 🚀 Future Enhancements

- Machine Learning based severity prediction
- Real-time Weather API integration
- Traffic-aware ambulance routing
- SMS & Email emergency alerts
- Multi-agent AI coordination
- Live GPS tracking of ambulances
- Predictive disaster analytics

---

# 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Full Stack Web Development
- REST API Development
- Flask Framework
- JavaScript DOM Manipulation
- Interactive GIS Mapping
- SQLite Database Management
- Git & GitHub Version Control
- Cloud Deployment using Render
- Problem Solving & Debugging

---

# 👩‍💻 Developed By

**Shreya Praruk**

Bachelor of Engineering

Artificial Intelligence & Machine Learning

CMR Institute of Technology

Bengaluru, India

---
