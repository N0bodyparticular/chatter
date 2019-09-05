@echo off
pyinstaller new_client_gui.py -F -w
pyinstaller new_gui_server.py -F -w
echo Build Complete