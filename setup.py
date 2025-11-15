from setuptools import setup, find_packages

setup(
    name="url_ai_checker",
    version="0.1.0",
    description="Librería con IA para revisar URLs.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Autor",
    license="MIT",
    python_requires=">=3.9",
    packages=find_packages(),
    install_requires=[
        "requests",
        "scikit-learn",
        "numpy",
        "networkx"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
