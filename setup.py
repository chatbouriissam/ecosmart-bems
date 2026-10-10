"""
Setup configuration for EcoSmart BEMS - Building Energy Management System.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="ecosmart-bems",
    version="1.0.0",
    author="ISSAM CHATBOURI",
    author_email="chatbouri.issam@gmail.com",
    description="EcoSmart BEMS - Building Energy Management System with ML-powered anomaly detection",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chatbouri-issam/ecosmart-bems",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Home Automation",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.7.0",
            "flake8>=6.0.0",
            "mypy>=1.5.0",
            "pre-commit>=3.3.0",
        ],
        "sensors": [
            "pyserial>=3.5",
            "paho-mqtt>=1.6.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "sbems=sbems.main:main",
            "sbems-server=sbems.api.server:main",
        ],
    },
    include_package_data=True,
    package_data={
        "sbems": ["config/*.yaml", "web/templates/*", "web/static/*"],
    },
)
