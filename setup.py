import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="event_utils",  # Replace with your own username
    version="0.1",
    author="Timo Stoffregen",
    description="Event utils",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TimoStoff/event_utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)