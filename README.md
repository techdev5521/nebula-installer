# Nebula Installer
A simple installer for the [Nebula](https://github.com/slackhq/nebula) mesh network binaries.

## Requirements
- Python >= 3.10
- Python venv

## Usage
**Make a directory**
Make a directory where you want Nebula to be installed. Some suggestions are:

- **Linux/macOS**: `/opt/nebula`
- **Windows**: `C:\Program Files\Nebula`

Once created, make sure that appropriate permissions are applied to the folder. Optionally, add the folder to your system's path.

**Install the Nebula Installer**
```bash
pip install git+git@bitbucket.org:allogy/nebula-installer.git
```

**Run the install command**
```bash
install-nebula
```

## Development
To contribue to the development of this project:

**Clone the repo**
```bash
git clone git@bitbucket.org:allogy/nebula-installer.git
```

**Enter the repo**
```bash
cd nebula-installer
```

**Create a Python virtual environment**
```bash
./rebuild_venv.sh
```