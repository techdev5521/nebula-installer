"""Installer for Nebula Binaries"""
import platform, tempfile, requests, wget, tarfile, zipfile, os
from pathlib import Path

def get_os() -> str:
    """Return the name of the OS."""
    supported_systems = ["windows", "linux", "darwin"]
    os = platform.system().lower()
    
    if os not in supported_systems:
        raise ValueError(f"{os} is not a supported operating system.")
    
    return os

def get_cpu() -> str:
    """Return the type of CPU."""
    cpu = platform.machine().lower()
    
    if cpu == "x86_64": # How Intel processors report 64bit
        cpu = "amd64"
    if cpu == "aarch64": # How Linux reports ARM 64bit
        cpu = "arm64"
    
    return cpu

def get_github_asset_name() -> str:
    """Returns the name of the Nebula asset to download.
    
        Examples: 
            - 'nebula-linux-arm64'
            - 'nebula-darwin`
    """
    os = get_os()
    cpu = get_cpu()

    # Filename always starts with `nebula-OS`
    file_string = f"nebula-{os}"

    # Add CPU type unless on macOS
    if os != "darwin":
        file_string += f"-{cpu}"

    return file_string

def get_download_url(asset_name: str) -> str:
    """Returns the latest download URL for the given asset name.
    
    Arguments:
        asset_name {str}: The name of the asset to download.

    Example:
        ```
        get_download_url('nebula-linux-arm64.tar.gz')
        ```
    """
    latest_release = requests.get("https://api.github.com/repos/slackhq/nebula/releases").json()[0]
    
    download_url = ""
    for asset in latest_release["assets"]:
        if asset["name"].startswith(asset_name):
            download_url = asset["browser_download_url"]
            break
    
    if download_url == "":
        raise ValueError(f"No asset named {asset_name} found.")
    
    return download_url

def extract_archive(path_to_archive: str, install_path: str) -> None:
    """Extract the contents of a downloaded archive."""
    path_to_archive = Path(path_to_archive)

    if path_to_archive.suffix == ".gz":
       with tarfile.open(path_to_archive) as archive:
            archive.extractall(install_path)
    
    if path_to_archive.suffix == ".zip":
        with zipfile.ZipFile(path_to_archive) as archive:
            archive.extractall(install_path)



# Set install directory to current directory
install_dir = Path(os.curdir).absolute()

# Get the name of the file to download
asset_name = get_github_asset_name()

# Get the download URL for the file
download_url = get_download_url(asset_name)

# Download the archive to a temporary directory
with tempfile.TemporaryDirectory() as temp_dir:
    print(f"Downloading {asset_name} from {download_url}")
    nebula_archive = wget.download(url=download_url, out=temp_dir)
    print() # Print an empty line because wget does not have a newline.
    extract_archive(nebula_archive, install_dir)
    print(f"Installed Nebula binaries at {install_dir}")