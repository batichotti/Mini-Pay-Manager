import subprocess
import PyInstaller.__main__

subprocess.check_call(['pip', 'install', '-r', 'requirements.txt'])

PyInstaller.__main__.run([
    '--name=%s' % 'MiniPayManager',
    '--onefile',
    '--windowed',
    '--icon=%s' % 'path/to/icon.ico',  # Update this path to your icon file
    '--add-data=%s' % 'src;src',
    'src/gui.py',
])
