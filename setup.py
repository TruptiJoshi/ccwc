from setuptools import setup, find_packages

setup(
    name="ccwc",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ccwc=ccwc.ccwc:main',  # This makes 'ccwc' available as a command
        ],
    },
    install_requires=[
        # List of dependencies
    ],
)
