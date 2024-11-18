import os
import sys
from subprocess import call, check_output
from sys import platform

from setuptools import find_packages, setup
from setuptools.command.install import install

REQUIRED_PACKAGES = ["numpy>=1.19.5", "scipy>=1.5.4", "h5py>=2.7.1", "scikit-learn>=0.23.2", "pandas>=1.1.3", "openpyxl>=3.1.5","nodejs>=20.17.0","matplotlib>=3.7.2","jupyter>=1.0.0","jupyterlab>=4.2.5","seaborn>=0.11.2","tensorflow>=>2.6.0","keras>=2.6.0","statsmodels>=0.12.2"]

PACKAGE_NAME = 'dpramp'
DESCRIPTION = 'Deterministic and probabilistic forecasting of wind power generation and ramp rate with expectation-implemented deep learning'
with open('README.md', encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()
AUTHOR = 'Min-Seung Ko, Hao Zhu, Kyeon Hur'
AUTHOR_EMAIL = 'kms4634500@utexas.edu'
URL = 'https://github.com/MinseungKo/Deterministic_and_probabilistic_forecasting_of_wind_power_generation_and_ramp_rate_with_expectation'
MINIMUM_PYTHON_VERSION = 3, 6  # Minimum of Python 3.6
VERSION = '0.1.0'


def check_python_version():
    """Exit when the Python version is too low."""
    if sys.version_info < MINIMUM_PYTHON_VERSION:
        sys.exit("Python {}.{}+ is required.".format(*MINIMUM_PYTHON_VERSION))


check_python_version()

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    install_requires=REQUIRED_PACKAGES,
    url=URL,
    license='MIT License',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6'
    ],
    include_dirs=[numpy.get_include()],
    python_requires='>=3.6',
    packages=find_packages()
)
