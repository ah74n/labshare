# 📁 LabShare - Local File Exchange Layer

<p align="center">
  <b>A lightweight file-sharing platform for computer labs and local networks.</b><br>
  Share files instantly across devices without USB drives, cloud storage, or email.
</p>

---

## ✨ Features

- 📤 Upload files from any device on the network
- 📥 Download shared files instantly
- 🗑️ Delete unwanted files
- 🌐 Access through any modern web browser
- ⚡ Lightweight Flask backend
- 🔒 Works entirely on your local Wi-Fi network
- 💻 Cross-platform (Windows, Linux & macOS)

---

## 🏗️ Architecture

```text
                 Local Wi-Fi Network

     +-------------------+
     |   Host Computer   |
     |-------------------|
     |   Flask Server    |
     |   app.py          |
     +---------+---------+
               |
     -----------------------------
      |          |          |
      |          |          |
+-----------+ +-----------+ +-----------+
| Client 1  | | Client 2  | | Client N  |
| Browser   | | Browser   | | Browser   |
+-----------+ +-----------+ +-----------+
```

The **host computer** runs the Flask server.

Every device connected to the **same local network** can access the shared files using a web browser.

---

# 🛠 Requirements

- Python 3.x
- Flask
- Windows 10/11, Linux, or macOS

---

# 🚀 Quick Start

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/LabShare.git
cd LabShare
```

---

## 2. Install Dependencies

```bash
pip install flask
```

---

## 3. Find Your Local IP Address

### Windows

```bash
ipconfig
```

Look for:

```
IPv4 Address
```

Example:

```
192.168.1.45
```

### Linux

```bash
ip a
```

or

```bash
ifconfig
```

### macOS

```bash
ifconfig
```

---

## 4. Start the Server

```bash
python app.py
```

The server will start on

```
http://0.0.0.0:8080
```

Keep this terminal open while the server is running.

---

# 🌐 Accessing LabShare

Any device connected to the **same Wi-Fi network** can open:

```
http://YOUR_LOCAL_IP:8080
```

Example:

```
http://192.168.1.45:8080
```

---

# 📤 Upload Files

1. Open LabShare in your browser.
2. Click the upload area.
3. Select a file.
4. Click **Upload**.

The file immediately becomes available to everyone on the network.

---

# 📥 Download Files

Click the **Download** button beside any shared file.

---

# 🗑 Delete Files

Click the **Delete** button next to the file.

A confirmation prompt prevents accidental deletion.

---

# 📂 Project Structure

```text
LabShare/
│
├── app.py               # Flask backend
├── shared_files/        # Uploaded files            
└── README.md
```

---

# ⚙️ How It Works

```text
          Upload File
               │
               ▼
        Flask Web Server
               │
      Stores in shared_files/
               │
               ▼
Clients download using browser
```

---

# 🔧 Troubleshooting

## Clients cannot connect

Make sure:

- All devices are connected to the same Wi-Fi network.
- The correct IP address is being used.
- Port **8080** is included.

Example:

```
http://192.168.1.45:8080
```

---

## Windows Firewall

Allow **Python** through Windows Defender Firewall when prompted.

---

## AP Isolation

Some institutional or public Wi-Fi networks enable **AP Isolation**, preventing devices from communicating with each other.

If this happens:

- Create a mobile hotspot.
- Connect all devices to that hotspot.
- Run the server again.

---

# 💡 Use Cases

- Computer Labs
- Classrooms
- Workshops
- Hackathons
- Team Collaboration
- Offline File Sharing

---

# 🧰 Built With

- Python
- Flask
- HTML
- CSS
- JavaScript

---

# 📜 License

This project is licensed under the MIT License.

---

<p align="center">
Made with ❤️ for classrooms, labs, and local collaboration.
</p>
