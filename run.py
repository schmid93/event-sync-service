import os
import platform
import shutil
import subprocess
import sys
import time
import webbrowser
from pathlib import Path

ROOT = Path(__file__).parent.resolve()


def print_header():
    print("=" * 60)
    print("🚀 Event Sync Service Launcher")
    print("=" * 60)


def get_python():
    """
    Returns the python executable inside backend/.venv
    """

    if platform.system() == "Windows":
        python = ROOT / "backend" / ".venv" / "Scripts" / "python.exe"
    else:
        python = ROOT / "backend" / ".venv" / "bin" / "python"

    return python


def validate_environment():

    python = get_python()

    if not python.exists():

        print("\n❌ Virtual environment not found.\n")

        print("Create it with:\n")

        print("cd backend")

        print("python -m venv .venv")

        if platform.system() == "Windows":
            print(r".venv\Scripts\activate")
        else:
            print("source .venv/bin/activate")

        print("pip install -r requirements.txt")

        sys.exit(1)

    npm = shutil.which("npm") or shutil.which("npm.cmd")

    if npm is None:

        print("\n❌ npm was not found.")

        print("Please install Node.js.")

        sys.exit(1)

    node_modules = ROOT / "frontend" / "node_modules"

    if not node_modules.exists():

        print("\n❌ Frontend dependencies not installed.\n")

        print("Run:")

        print("cd frontend")

        print("npm install")

        sys.exit(1)

    return python, npm


def main():

    print_header()

    python, npm = validate_environment()

    print("\nStarting backend...")

    backend = subprocess.Popen(
        [
            str(python),
            "-m",
            "uvicorn",
            "app.main:app",
            "--reload",
        ],
        cwd=ROOT / "backend",
    )

    print("✅ Backend started.")

    print("\nStarting frontend...")

    frontend = subprocess.Popen(
        [
            npm,
            "run",
            "dev",
        ],
        cwd=ROOT / "frontend",
    )

    print("✅ Frontend started.")

    print("\nWaiting a few seconds before opening the browser...")

    time.sleep(4)

    webbrowser.open("http://localhost:5173")

    print("\n" + "=" * 60)
    print("Backend : http://localhost:8000")
    print("Frontend: http://localhost:5173")
    print("=" * 60)
    print("\nPress Ctrl+C to stop both services.\n")

    try:

        while True:
            time.sleep(1)

    except KeyboardInterrupt:

        print("\nShutting down...")

        backend.terminate()
        frontend.terminate()

        backend.wait()
        frontend.wait()

        print("Done 👋")


if __name__ == "__main__":
    main()