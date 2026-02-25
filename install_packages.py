#!/usr/bin/env python
"""
Package Installation Script for Food Delivery Operations Analytics
Installs all required packages from requirements.txt
"""

import subprocess
import sys

def install_packages():
    """Install all packages from requirements.txt"""
    
    # List of packages to install (grouped by category)
    core_packages = [
        'python-dotenv',
        'pydantic',
    ]
    
    database_packages = [
        'sqlalchemy',
        'psycopg2-binary',
    ]
    
    data_packages = [
        'pandas',
        'numpy',
    ]
    
    visualization_packages = [
        'plotly',
        'altair',
    ]
    
    security_packages = [
        'cryptography',
        'bcrypt',
    ]
    
    testing_packages = [
        'pytest',
        'pytest-cov',
    ]
    
    code_quality_packages = [
        'black',
        'flake8',
    ]
    
    utility_packages = [
        'requests',
        'click',
        'pyyaml',
        'jsonschema',
    ]
    
    all_packages = (
        core_packages +
        database_packages +
        data_packages +
        visualization_packages +
        security_packages +
        testing_packages +
        code_quality_packages +
        utility_packages
    )
    
    print("[*] Installing Food Delivery Operations Analytics packages...")
    print(f"[*] Total packages to install: {len(all_packages)}")
    
    # Install in batches
    batch_size = 5
    for i in range(0, len(all_packages), batch_size):
        batch = all_packages[i:i+batch_size]
        print(f"\n[*] Installing batch {i//batch_size + 1}: {', '.join(batch)}")
        
        cmd = [sys.executable, '-m', 'pip', 'install', '--user', '--no-warn-script-location'] + batch
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"    [OK] Batch {i//batch_size + 1} installed successfully")
        else:
            print(f"    [WARNING] Batch {i//batch_size + 1} had issues (continuing...)")
            if result.stderr:
                print(f"    Error: {result.stderr[:200]}")
    
    print("\n[*] Installing web frameworks (optional)...")
    web_packages = ['streamlit', 'dash']
    for pkg in web_packages:
        print(f"    Installing {pkg}...")
        cmd = [sys.executable, '-m', 'pip', 'install', '--user', '--no-warn-script-location', pkg]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"    [OK] {pkg} installed")
        else:
            print(f"    [SKIP] {pkg} (optional, can be installed later)")
    
    print("\n[*] Package installation complete!")
    print("[*] Verifying core packages...")
    
    # Verify core packages
    verify_packages = ['pandas', 'numpy', 'pydantic', 'sqlalchemy']
    all_good = True
    for pkg in verify_packages:
        try:
            __import__(pkg)
            print(f"    [OK] {pkg} is available")
        except ImportError:
            print(f"    [FAIL] {pkg} is NOT available")
            all_good = False
    
    if all_good:
        print("\n[OK] All core packages installed successfully!")
    else:
        print("\n[WARNING] Some packages are missing. Try running:")
        print("    python -m pip install -r requirements.txt --upgrade --user")

if __name__ == '__main__':
    install_packages()
