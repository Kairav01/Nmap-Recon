import os
import subprocess

def run_scan():
    # Automatically search common Nmap installation paths on Windows
    possible_paths = [
        r"C:\Program Files\Nmap\nmap.exe",
        r"C:\Program Files (x86)\Nmap\nmap.exe"
    ]
    
    nmap_path = None
    for path in possible_paths:
        if os.path.exists(path):
            nmap_path = path
            break
            
    # If Nmap still isn't found, print a friendly error instead of crashing
    if not nmap_path:
        print("[-] Error: nmap.exe could not be found automatically.")
        print("Please verify where Nmap is installed on your computer.")
        return

    print(f"[+] Found Nmap at: {nmap_path}")
    print("Starting Nmap local network scan...")
    
    target = input("Enter IP Addres: ")  # Scanning localhost safely for demonstration
    command = [nmap_path, "-sS", "-sV", target]
    
    try:
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print("\n--- Scan Results ---")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"[-] Nmap ran into an error:\n{e.stderr}")

if __name__ == "__main__":
    run_scan()