from setuptools import setup, find_packages

# Define Dependencies for Extra Requires
conditional_dependencies = {
    "dev":[
        
    ]
}

def get_all_dependencies() -> list:
    """Returns a single array of all dependencies."""
    dependencies = []
    for condition in conditional_dependencies.keys():
        dependencies += conditional_dependencies[condition]
    return dependencies

setup(
    name="Nebula Installer",
    version="1.0.0",
    description="A cross platform installer for Nebula client binaries.",
    python_requires='>=3.6',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires = [

    ],
    extras_require={
        "dev": conditional_dependencies["dev"],
        "all": get_all_dependencies()
    },
    entry_points={
        "console_scripts": [
            "nebula-install = nebula_installer.install:install"
        ]
    }
)