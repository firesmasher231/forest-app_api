from setuptools import setup, find_packages

setup(
    name="forest_app",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["requests>=2.25.0"],
    author="Your Name",
    author_email="your.email@example.com",
    description="Unofficial Python client for Forest App API",
    long_description="A Python client for interacting with the Forest App API",
    url="https://github.com/yourusername/forest_app",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/forest_app/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    keywords="forest app, productivity, time tracking, api client",
) 