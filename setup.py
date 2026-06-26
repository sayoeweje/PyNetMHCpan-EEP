from setuptools import setup, find_packages

setup(
    name='PyNetMHCpan-EEP',
    version='0.2.0',
    packages=find_packages(),
    url='https://github.com/sayoeweje/PyNetMHCpan-EEP',
    python_requires='>=3.7',
    license='MIT',
    author='Feyisayo Eweje',
    include_package_data=True,
    author_email='',
    description='Modified implementation of PyNetMHCpan for use in iterative mutagenesis peptide optimization studies.',
    install_requires=["numpy", "pandas"]
)
