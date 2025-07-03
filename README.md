# 🧠 Multi-Agent Query System

An AI-powered assistant system leveraging two specialized [CrewAI](https://docs.crewai.com) agents — **Support Agent** and **Dashboard Agent** — designed to handle natural language queries, interact with MongoDB, and power intelligent dashboards for business analytics and operations.

---

## 🚀 Features

- 🤖 **Multi-Agent Architecture** using CrewAI
- 💬 **Natural Language Query Processing**
- 📊 **Dashboard Agent**: Provides insights & metrics from MongoDB (e.g., revenue, clients, attendance)
- 🛠 **Support Agent**: Handles support-related queries and triggers external API actions
- 🔗 **External API Integration**: Enables real-time actions like booking, class creation, etc.
- 📈 **Visual Analytics Dashboards**
- 🌐 Fully integrated **React + TailwindCSS frontend**
- ⚡ Built with **FastAPI** and connected to **MongoDB**

---

## ⚙️ Tech Stack

| Layer       | Technology            |
|-------------|------------------------|
| Frontend    | React, TailwindCSS     |
| Backend     | FastAPI (Python)       |
| Agents      | CrewAI (LLM-powered)   |
| Database    | MongoDB                |

---

## 🧩 Agents Overview

### 📬 Support Agent

- Responds to general support queries
- Can initiate external API calls (e.g., booking a class, adding clients)
- Uses natural language understanding to guide actions

### 📊 Dashboard Agent

- Performs real-time data aggregation on MongoDB
- Generates insights such as:
  - Revenue Metrics
  - Active/Inactive Client Ratio
  - Birthday Reminders
  - New Clients This Month
- Responds with concise summaries or JSON for visualization

---

## 🛠 Project Structure
```bash
backend/
│
├── api/
│   ├── main.py               # FastAPI entry point
│   └── routes.py             # API routes for /query and /add
│
├── agents/
│   ├── support_agent.py      # Handles support queries (classes, orders, clients)
│   └── dashboard_agent.py    # Handles metrics/analytics
│
├── tools/
│   ├── mongodb_tool.py       # MongoDB tool for CrewAI
│   └── external_api.py       # Tool to simulate order/client creation
│
└── utils/
    └── schema.py             # Sample MongoDB mock data
```
## 🚀 Getting Started

Follow these steps to set up and run the Multi-Agent Query System locally.

---

### 1. 📥 Clone the Repository

```bash
git clone https://github.com/your-username/multi-agent-query-system.git
cd qest-assignment
cd backend
pip install -r requirements.txt
pip install fastapi uvicorn pymongo pydantic crewai
uvicorn api.main:app --reload
cd frontend
npm install
npm run dev   # or npm start
```
## 📸 Screenshots
---
![Alt text](https://github.com/vik802207/qest-assignment/blob/main/img/Screenshot%20(606).png?raw=true)
![Alt text](https://github.com/vik802207/qest-assignment/blob/main/img/Screenshot%20(607).png?raw=true)
![Alt text](https://github.com/vik802207/qest-assignment/blob/main/img/Screenshot%20(608).png?raw=true)
![Alt text](https://github.com/vik802207/qest-assignment/blob/main/img/Screenshot%20(609).png?raw=true)
![Alt text](https://github.com/vik802207/qest-assignment/blob/main/img/Screenshot%20(610).png?raw=true)
![Alt text](https://github.com/vik802207/qest-assignment/blob/main/img/Screenshot%20(611).png?raw=true)
![Alt text](https://github.com/vik802207/qest-assignment/blob/main/img/Screenshot%20(612).png?raw=true)
![Alt text](https://github.com/vik802207/qest-assignment/blob/main/img/Screenshot%20(613).png?raw=true)
![Alt text](https://github.com/vik802207/qest-assignment/blob/main/img/Screenshot%20(614).png?raw=true)
![Alt text](https://github.com/vik802207/qest-assignment/blob/main/img/Screenshot%20(615).png?raw=true)
![Alt text](https://github.com/vik802207/qest-assignment/blob/main/img/Screenshot%20(616).png?raw=true)
![Alt text](https://github.com/vik802207/qest-assignment/blob/main/img/Screenshot%20(617).png?raw=true)
![Alt text](https://github.com/vik802207/qest-assignment/blob/main/img/Screenshot%20(618).png?raw=true)
![Alt text](https://github.com/vik802207/qest-assignment/blob/main/img/Screenshot%20(619).png?raw=true)

---

## 🧠 Agents

### 🤖 Support Agent

The **Support Agent** handles operational and customer service tasks using natural language inputs. It can **read from** and **write to MongoDB**, and also **trigger external API actions**.

#### 💡 Example Queries:
- `"What classes are available this week?"`
- `"Show payment for order #12345"`
- `"Create an order for Yoga Beginner for client Priya Sharma"`
- `"Add a new client named Priya Sharma with phone 9991234567"`

#### 🛠 Capabilities:
- Look up available classes
- Fetch order or payment info
- Add new clients or orders
- Interface with external APIs (e.g., booking, enrollment)

---

### 📊 Dashboard Agent

The **Dashboard Agent** is focused on generating **business insights and analytics** from MongoDB. It performs advanced **aggregation queries** and returns insights in both raw and visual format.

#### 📈 Example Queries:
- `"How much revenue did we generate this month?"`
- `"Which course has the highest enrollment?"`
- `"Attendance percentage for Pilates?"`
- `"Active vs inactive clients count?"`
- `"New clients this month?"`

#### 📊 Capabilities:
- Revenue and payment analytics
- Enrollment and attendance stats
- Client activity monitoring
- Aggregated data summaries for dashboards

---

## 🤝 Contributing
Pull requests are welcome. For major changes, open an issue first to discuss what you would like to change.

## 📜 License
This project is licensed under the MIT License.
## 🔗 Live Demo
## [![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen?style=for-the-badge)](https://qest-assignment-henna.vercel.app/)

## 👨‍💻 Author
Developed by Vikash Gupta
📧 Contact: vikashg802207@gmail.com




