#!/bin/bash

APP_NAME="sap"

# Paths
BINARY_SRC="$APP_NAME"
ICON_SRC="app_icon.png"

# Destination paths
BIN_DIR="$HOME/.local/bin/"
ICON_DIR="$HOME/.local/share/icons/"
ICON_DEST="$HOME/.local/share/icons/$ICON_SRC"
DESKTOP_DIR="$HOME/.local/share/applications"
DESKTOP_FILE="$DESKTOP_DIR/$APP_NAME.desktop"

# Create necessary directories
mkdir -p "$BIN_DIR" "$ICON_DIR" "$DESKTOP_DIR"

# Copy binary
cp "$BINARY_SRC" "$BIN_DIR"
chmod +x "$BIN_DIR/$APP_NAME"

# Copy icon
cp "$ICON_SRC" "$ICON_DEST"

# Create .desktop file with absolute paths
cat > "$DESKTOP_FILE" <<EOL
[Desktop Entry]
Name=$APP_NAME
Comment=Simple Audio Player app made with python, by ibrahimmoalim@github
Exec=$BIN_DIR/$APP_NAME
Icon=$ICON_DEST
Type=Application
Categories=AudioVideo;Player;
Terminal=false
StartupWMClass=sap
EOL

# Make the .desktop file executable
chmod +x "$DESKTOP_FILE"

# Update desktop database
update-desktop-database "$DESKTOP_DIR" 2>/dev/null

# Create an alias to run the app easily from terminal
grep -qxF "alias sap='setsid ~/.local/bin/sap >/dev/null 2>&1 &'" ~/.bashrc || \
printf "\nalias sap='setsid ~/.local/bin/sap >/dev/null 2>&1 &'\n" >> ~/.bashrc

echo "$APP_NAME has been installed!"
echo "You can now search for $APP_NAME in your application menu."
