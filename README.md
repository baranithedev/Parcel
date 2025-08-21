# PARCEL - File Sharer

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=ffdd54)

**Parcel** is a socket-based file transfer tool designed to share files efficiently between devices over a network. It focuses on speed, simplicity, and reliability, without relying on third-party cloud services

### Features
- ### **File Transfer**
    - Send/receive single file.
    - Support for large files (tested up to 4.18 GB).
    - Progress tracking with speed, size, and percentage.

- ### **Cross-Platform**
    - Works on Windows, Linux, macOS, and Android (via Termux).
    - Pure Python implementation (no heavy dependencies).

### **Technical Specifications**
- Transfer Speed: ~10 minutes for 4.18 GB (≈ 7 MB/s over Wi-Fi LAN) without internet
- OS Compatibility:<br/>
    - Windows
    - Linux distros (Debian/Ubuntu/Fedora etc.)
    - macOS
    - Android (Termux)

### Usage
### *Send* 
```bash
python parcel --host <ip> --mode <mode> --file <file>.*
```
Example: python parcel --host 192.168.0.2 --mode send --file movie.mp4

### *Receive*
```bash
python parcel --connect <sender_ip> --mode <mode> --pair <pair_code>
```
Example: python parcel --connect 192.168.0.2 --mode receive --pair 64556

### Performance
- **Test Case:** 4.18 GB file over Wi-Fi without internet
- **Transfer Time:** ~10 minutes
- **Average Speed:** 6–7 MB/s
