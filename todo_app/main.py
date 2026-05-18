#!/usr/bin/env python3
"""
EasyToDo - Simple To-Do List Application with Dual Storage
Author: clauswitfelt
GitHub: https://github.com/clauswitfelt/EasyDB
"""

import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from gui.main_window import TodoApp

def main():
    """Launch the EasyToDo application"""
    app = TodoApp()
    app.run()

if __name__ == "__main__":
    main()
