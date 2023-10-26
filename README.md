# Nebula Installer
A simple installer for the [Nebula](https://github.com/slackhq/nebula) mesh network binaries.

## Requirements
- Python >= 3.10
- Python venv

## Usage
**Make a Directory**<br />
Make a directory where you want Nebula to be installed. Some suggestions are:

- **Linux/macOS**: `/opt/nebula`
- **Windows**: `C:\Program Files\Nebula`

Once created, check that permission will allow you to read, write and execute from in that directoy. 

**Install the Nebula Installer**
```bash
pip install git+git@bitbucket.org:allogy/nebula-installer.git
```

**Run the Install Command in the Install Directory**
```bash
cd /opt/nebula
install-nebula
```

After successful installation, you will have the two Nebula binaries in the install directory:

```bash
$ ls
nebula
nebula-cert
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