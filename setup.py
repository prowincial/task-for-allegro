import setuptools
import pathlib

README = (pathlib.Path(__file__).parent / "README.md").read_text()

setuptools.setup(
    name="MServer",
    version="0.1.0",
    author="Maksim Shumak",
    description="Description",
    long_description=README,
    long_description_content_type="text/markdown",
    url="github link",
    packages=setuptools.find_packages(),
    install_requires=["flask"],
    install_package_data=True,
    license='Apache 2.0',
    license_file='./LICENSE',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Apache2",
    ],
)