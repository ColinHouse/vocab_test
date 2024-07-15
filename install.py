import os
import subprocess
import sys


def install_requirements():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])


def check_pyinstaller():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "show", "pyinstaller"])
    except subprocess.CalledProcessError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])


def create_executable():
    subprocess.check_call(["pyinstaller", "--onefile", "--windowed", "main.py"])


def main():
    install_requirements()
    os.makedirs('vocabs', exist_ok=True)

    create_exe = input("Do you want to create an executable? (y/n): ").strip().lower()
    if create_exe == 'y':
        check_pyinstaller()
        create_executable()


if __name__ == "__main__":
    main()
