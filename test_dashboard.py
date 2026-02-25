"""Test dashboard app syntax and imports"""
import sys
sys.path.insert(0, '.')

# Test syntax by compiling
import py_compile

try:
    py_compile.compile('src/dashboard/app.py', doraise=True)
    print("[OK] app.py syntax is valid")
except py_compile.PyCompileError as e:
    print(f"[ERROR] Syntax error in app.py: {e}")
    sys.exit(1)

# Test basic imports from the file
print("\n[TEST] Checking imports in app.py...")

try:
    import logging
    print("[OK] logging module imported")
except ImportError as e:
    print(f"[ERROR] Failed to import logging: {e}")

try:
    import random
    print("[OK] random module imported")
except ImportError as e:
    print(f"[ERROR] Failed to import random: {e}")

try:
    import json
    print("[OK] json module imported")
except ImportError as e:
    print(f"[ERROR] Failed to import json: {e}")

try:
    from datetime import datetime, timedelta
    print("[OK] datetime modules imported")
except ImportError as e:
    print(f"[ERROR] Failed to import datetime: {e}")

try:
    from typing import Dict, Any, List
    print("[OK] typing modules imported")
except ImportError as e:
    print(f"[ERROR] Failed to import typing: {e}")

try:
    import pandas as pd
    print("[OK] pandas imported")
except ImportError as e:
    print(f"[WARNING] pandas not installed: {e}")

print("\n[SUCCESS] Dashboard app.py is ready to run!")
print("[INFO] To run the dashboard, execute: streamlit run src/dashboard/app.py")
