# Simple Audio Player (SAP)

A lightweight standalone **audio player for Linux/Windows**.

---

## Table of Contents

* [Features](#features)
* [Installation for Linux](#installation-for-linux)
* [Installation for Windows](#installation-for-windows)

---

## Features

* Play audio files (MP3, WAV, etc.) from a *manually chosen folder*
* The folder should contain *only audio files*
* Simple and intuitive interface
* Lightweight and fast
* Supports *only play, pause/resume, skip, and stop* functions
* Does not include a *slider* to jump to a *specific timestamp* in the audio

---

# Installation for Linux

1. **Download the latest release** from the [Releases page](https://github.com/ibrahimmoalim/simple_audio_player/releases/tag/v2.4)

2. **Extract the downloaded ZIP file**:

## Unzip into sap (folder)
```bash
unzip sap.zip
```

## Navigate into the folder
```bash
cd sap
```

3. **Run the install script**:

## Make the install script executable
```bash
chmod +x install.sh
```
## Run the install script to set up the binary and icon
```bash
./install.sh
```

The script will:

* Copy the executable to `~/.local/bin`
* Copy the icon to `~/.local/share/icons`
* Create a `.desktop` file in `~/.local/share/applications`
* Update the desktop database so you can launch the app from your menu

You can now search for **sap** in your application menu and run it.

---

## Running the App on Linux

You can launch **sap** in two ways:

 - **From the application menu using the icon created by the install script**

 - **Or directly from the terminal**
```bash
sap
```

---

# Installation for Windows

1. **Download the latest release** from the [Releases page](https://github.com/ibrahimmoalim/simple_audio_player/releases/tag/v1.0-windows)

2. **Extract the downloaded ZIP file**

3. **Run the SAP application**

---
