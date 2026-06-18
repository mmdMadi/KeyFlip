import os
import sys
import platform
import logging
from pathlib import Path

def get_app_executable_path():
    """Get the path to the current application executable"""
    if getattr(sys, 'frozen', False):
        # Running as compiled executable
        return sys.executable
    else:
        # Running as script - return the main.py path
        return os.path.abspath(os.path.join(os.path.dirname(__file__), 'main.py'))

def check_startup_status(app_name="Transliterator"):
    """Check if the app is in Windows startup"""
    if platform.system().lower() != "windows":
        return {"error": "Startup management only available on Windows"}
    
    try:
        import winreg
        app_path = get_app_executable_path()
        startup_folder = os.path.join(
            os.getenv('APPDATA'),
            r'Microsoft\Windows\Start Menu\Programs\Startup'
        )
        shortcut_path = os.path.join(startup_folder, f"{app_name}.lnk")
        exists = os.path.exists(shortcut_path)
        
        logging.info(f"Checking startup status for: {app_path}")
        logging.info(f"Startup folder: {startup_folder}")
        logging.info(f"Shortcut path: {shortcut_path}")
        logging.info(f"Shortcut exists: {exists}")
        
        return {
            "in_startup": exists,
            "shortcut_path": shortcut_path.replace('\\', '/'),
            "app_path": app_path.replace('\\', '/')
        }
    except Exception as e:
        error_msg = f"Error checking startup status: {e}"
        logging.error(error_msg, exc_info=True)
        return {"error": error_msg}

def add_to_startup(app_name="Transliterator"):
    """Add the app to Windows startup"""
    if platform.system().lower() != "windows":
        return {"error": "Startup management only available on Windows"}
    
    try:
        # Test if we're running in exe mode
        is_exe = getattr(sys, 'frozen', False)
        logging.info(f"Running in exe mode: {is_exe}")
        logging.info(f"Python executable: {sys.executable}")
        logging.info(f"Script path: {__file__}")
        
        # Try to import win32com components
        try:
            import win32com.client
            import pythoncom
            import pywintypes
            logging.info("Successfully imported win32com components")
        except ImportError as ie:
            error_msg = f"Failed to import win32com: {ie}"
            logging.error(error_msg)
            return {"error": error_msg}
        
        app_path = get_app_executable_path()
        startup_folder = os.path.join(
            os.getenv('APPDATA'),
            r'Microsoft\Windows\Start Menu\Programs\Startup'
        )
        shortcut_path = os.path.join(startup_folder, f"{app_name}.lnk")
        
        logging.info(f"Attempting to add to startup: {app_path}")
        logging.info(f"Startup folder: {startup_folder}")
        logging.info(f"Shortcut path: {shortcut_path}")
        
        if not os.path.exists(app_path):
            return {"error": f"Application path {app_path} does not exist"}
        
        # Ensure startup folder exists
        os.makedirs(startup_folder, exist_ok=True)
        
        # Initialize COM
        try:
            pythoncom.CoInitialize()
            logging.info("COM initialized successfully")
        except Exception as com_e:
            logging.warning(f"COM initialization warning: {com_e}")
        
        # Create shortcut
        try:
            shell = win32com.client.Dispatch("WScript.Shell")
            logging.info("WScript.Shell dispatch successful")
            
            shortcut = shell.CreateShortCut(shortcut_path)
            shortcut.Targetpath = app_path
            shortcut.WorkingDirectory = os.path.dirname(app_path)
            shortcut.save()
            
            logging.info(f"Added {app_name} to startup successfully")
            return {"success": True, "message": f"Added {app_name} to startup"}
            
        except Exception as shell_e:
            error_msg = f"Error creating shortcut: {shell_e}"
            logging.error(error_msg, exc_info=True)
            return {"error": error_msg}
        
    except ImportError as ie:
        error_msg = f"win32com not available: {ie}. Install with: pip install pywin32"
        logging.error(error_msg)
        return {"error": error_msg}
    except Exception as e:
        error_msg = f"Error adding to startup: {e}"
        logging.error(error_msg, exc_info=True)
        return {"error": error_msg}
