import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sha256_check",
    author="federicotorrielli",
    author_email="evilscript@protonmail.com",
    version="0.2",
    description="Quick SHA256 hash check",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/federicotorrielli/sha256_check",
    packages=["sha256_check"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "sha256_check = sha256_check.cli:main"
        ]
    },
    python_requires='>=3.6',
    install_requires=["colorama>=0.4.3"]
)
