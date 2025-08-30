# Crop Recommendation System

## Overview
The **Crop Recommendation System** is a web-based application built using **Django** and **Python**. It helps farmers and users identify the best crop to plant based on soil parameters (NPK, pH), weather conditions, and rainfall. The system also provides sowing and harvesting time suggestions along with mandi price information for better decision-making.

---

## Features
- Predicts the most suitable crop based on soil, temperature, humidity, and rainfall.
- Fetches temperature and humidity automatically using OpenWeatherMap API.
- Provides best sowing and harvesting time for recommended crops.
- Displays mandi price information for crops.
- User-friendly interface with simple navigation.
- Admin module to manage crops and mandi prices (optional).

---

## Tech Stack
- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Database:** SQLite (default) or can be configured for MySQL/PostgreSQL
- **Machine Learning:** Trained ML model (`model.pkl`) for crop prediction
- **APIs:** OpenWeatherMap for weather data, dummy APIs for Soil NPK and Rainfall

---


