from setuptools import setup, find_packages
with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(
    name='python_package',
    version='0.1.0',
    packages=find_packages(),
    install_requires=install_requires,
    extras_require={
        'dev': [
            'pytest',
        ]
    },
    python_requires='>=3.6',
)
