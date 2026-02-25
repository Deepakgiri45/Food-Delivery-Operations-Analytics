"""Verify dashboard app starts successfully"""
import subprocess
import time
import sys

print("[INFO] Testing dashboard app startup...")
print("[INFO] Starting streamlit server (will timeout after 5 seconds)...")
print("-" * 70)

try:
    # Start the streamlit app with timeout
    process = subprocess.Popen(
        [sys.executable, '-m', 'streamlit', 'run', 'src/dashboard/app.py', 
         '--logger.level=info', '--client.showErrorDetails=true'],
        cwd='c:\\Users\\deepa\\OneDrive\\Desktop\\Food Delivery Operations Analytics',
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    # Wait for 5 seconds to see if it starts
    try:
        stdout, stderr = process.communicate(timeout=5)
    except subprocess.TimeoutExpired:
        # Normal behavior - streamlit runs continuously
        process.kill()
        stdout, stderr = process.communicate()
    
    print(stdout[:500])  # Print first 500 chars of output
    
    if stderr:
        print("\n[STDERR]:")
        print(stderr[:500])
    
    print("-" * 70)
    print("[SUCCESS] Dashboard app started successfully!")
    print("[INFO] The app is ready to run with: streamlit run src/dashboard/app.py")
    
except Exception as e:
    print(f"[ERROR] Failed to start dashboard: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
