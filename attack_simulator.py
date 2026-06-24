import requests
import time

TARGET_URL = "http://127.0.0.1:5000/login"

def brute_force(username="alice", attempts=30, delay=0.1):
    passwords = [f"wrong-pass-{i}" for i in range(attempts)]

    print(f"[+] Sending {attempts} failed login attempts to {TARGET_URL}")
    print("[+] Watch the AI Guard dashboard at http://127.0.0.1:5001/admin?key=changeme")

    for pwd in passwords:
        data = {
            "username": username,
            "password": pwd
        }
        try:
            r = requests.post(TARGET_URL, data=data, timeout=5)
            print(f"Tried {username}:{pwd}, status={r.status_code}")
            if r.status_code == 403:
                print("[+] AI Guard blocked this IP. Stopping simulator.")
                break
        except Exception as e:
            print("Error:", e)
            break

        time.sleep(delay)

if __name__ == "__main__":
    brute_force()
