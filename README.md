# 🏬 Mall Indoor Navigation System (QR-Based Demo)

A web-based indoor navigation demo for shopping malls built using **Python (Flask)** and **QR Code scanning**.
This project demonstrates how users can scan a QR code at their current location and receive the shortest navigation path to a selected destination inside a mall.

This project is designed as a **demo-ready prototype** to showcase indoor navigation concepts to clients before full-scale implementation.

---

## 🚀 Features

* 📷 QR Code based location detection
* 🧭 Shortest path navigation using Dijkstra’s Algorithm
* 🌐 Web-based interface
* 🏬 Simulated mall layout
* 📱 Mobile and desktop compatible
* ⚡ Fast demo setup for client presentations

---

## 🧠 How It Works

1. QR codes are placed at key locations inside the mall (Entrance, Lift, Stores, Food Court, etc.).
2. User scans the QR code using the web application.
3. The scanned QR sets the user's current location.
4. User selects destination shop.
5. System calculates shortest path using graph-based navigation.
6. Route is displayed on screen.

The mall layout is represented as a **graph**, where:

* Nodes = Locations
* Edges = Walkable paths
* Weights = Distance between locations

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS, JavaScript
* **Navigation Logic:** NetworkX (Dijkstra Algorithm)
* **QR Scanner:** html5-qrcode
* **QR Generator:** Python qrcode library

---

## 📂 Project Structure

```
mall_navigation/
│
├── app.py
├── generate_qr.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/mall_navigation.git
cd mall_navigation
```

### 2️⃣ Install Dependencies

```bash
pip install flask networkx qrcode pillow
```

### 3️⃣ Generate QR Codes

```bash
python generate_qr.py
```

### 4️⃣ Run Application

```bash
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

Allow camera permission to scan QR codes.

---

## 📸 Demo Flow

1. Scan QR at current location
2. Select destination
3. Click Navigate
4. View shortest path

---

## 🔮 Future Improvements

* Real mall floor map visualization
* Multi-floor navigation support
* AR-based navigation
* BLE beacon integration
* Admin dashboard for shop management
* Real-time crowd-aware routing

---

## 👨‍💻 Author

**Sudeep Bhimannavar**

Indoor Navigation Demo Project
