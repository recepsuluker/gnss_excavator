# Localization of Excavator using GNSS & RTK

This project was developed as part of research work at The Julius Maximilians University of Würzburg. It focuses on estimating the 6-DoF pose of an excavator using multi-GNSS receivers and RTK corrections, integrated with a Raspberry Pi and ROS.

## 🚀 Project Overview
- High-precision real-time localization using GNSS with RTK.
- Integration with Raspberry Pi and ROS Noetic.
- Tested in both simulation (aluminum frame) and real environment (bicycle-mounted system).

## 📦 Structure
- `scripts/`: Python/ROS scripts for GNSS data parsing and pose calculation.
- `config/`: RTK base station and GNSS receiver configuration files.
- `data/`: Sample NMEA logs and processed test results.
- `launch/`: ROS launch files for initializing GPS nodes and publishers.
- `images/`: Test rig photos and system diagrams.

## 🧪 Test Setup
We used:
- A 1x1 meter aluminum frame with 3 GNSS receivers to simulate mounting on an excavator.
- A Raspberry Pi for data processing.
- RTK testing was also conducted using a bicycle-mounted GNSS system across campus, referencing a fixed base station.

## 🛰️ GNSS Details
- NMEA messages used: `$GGA`, `$VTG`, `$ZDA`.
- Real-time correction via RTK base station to enhance precision (~20%).

## 🔗 Future Work
- IMU sensor fusion for full 6-DoF orientation tracking.
- Visual SLAM integration in GPS-denied environments.

## 📷 Image
![Test Setup](images/test_frame.png)

---

Developed with ❤️ during a research assistantship in Würzburg, Germany.
