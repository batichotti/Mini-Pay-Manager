import subprocess
import PyInstaller.__main__

# Install dependencies
subprocess.check_call(['pip', 'install', '-r', 'requirements.txt'])

# Create executable
PyInstaller.__main__.run([
    '--name=%s' % 'MiniPaymentManager',
    '--onefile',
    '--windowed',
    '--icon=%s' % 'res\icon.ico',  # Update this path to your icon file
    '--add-data=%s' % 'src;src',
    'src/gui.py',
])
