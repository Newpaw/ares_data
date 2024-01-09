from setuptools import setup, find_packages

setup(
    name='ares_data',
    version='0.1.0',
    author='Jan Novopacký',
    author_email='jan.novopacky@gmail.com',
    description='`ares_data` je Python knihovna pro snadné získávání dat o společnostech z Českého obchodního rejstříku ARES.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='URL vašeho projektu na GitHubu',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    classifiers=[
        # Klasifikátory pro PyPI
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)