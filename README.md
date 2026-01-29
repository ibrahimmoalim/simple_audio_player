# Simple Audio Player (SAP)

A lightweight standalone **audio player for Linux**. No Python installation is required — the app comes as a ready-to-run executable.

---

## Features

* Play audio files (MP3, WAV, etc.)
* Simple and intuitive interface
* Lightweight and fast
* Creates a desktop menu icon for easy launching

---

## Installation

1. **Download the latest release** from the [Releases page](https://github.com/ibrahimmoalim/simple-audio-player/releases).

2. **Extract the downloaded ZIP file**:

# Unzip the release into a folder
```bash
unzip sap.zip -d sap
```

# Navigate into the folder
```bash
cd sap
```

3. **Run the install script**:

# Make the install script executable
```bash
chmod +x install.sh
```
# Run the install script to set up the binary and icon
```bash
./install.sh
```

The script will:

* Copy the executable to `~/.local/bin`
* Copy the icon to `~/.local/share/icons`
* Create a `.desktop` file in `~/.local/share/applications`
* Update the desktop database so you can launch the app from your menu

You can now search for **SAP** in your application menu and run it.

---

## Running the App

You can launch SAP in two ways:

 - **From the application menu using the icon created by the install script**

 - **Or directly from the terminal**
```bash
~/.local/bin/SAP
```

---
