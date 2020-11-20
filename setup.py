from setuptools import setup


def readfile(filename):
    with open(filename, 'r+') as f:
        return f.read()


setup(
    name="enable-disable-network-adapter",
    version="2020.11.18",
    description="Enable or disable Wi-Fi and Ethernet network adapters on Windows 10 with Python",
    long_description=readfile('README.md'),
    author="Heidi Ngew",
    install_requires=[
        'Click',
    ],
    py_modules=['main'],
    license=readfile('LICENSE'),
    entry_points={
        'console_scripts': [
            'enable-disable-network-adapter = main:change_adapter_options'
        ]
    },
)
