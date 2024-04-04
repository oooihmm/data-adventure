import subprocess
import time

def execute_script(script_name):
    print(f"Executing {script_name}")
    subprocess.Popen(["python", script_name])  
def main():
    scripts = [
        "steam-game-crawler.py",
        "steam-game-extractor.py",
        "steam-review-crawler.py",
        "steam-review-extractor.py"
    ]

    for script in scripts:
        execute_script(script)
        time.sleep(30)  

    print("All scripts initiated. Running concurrently.")
    time.sleep(10) 

if __name__ == "__main__":
    main()
