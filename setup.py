from setuptools import setup, find_packages

setup(
    name='better_sqlite',
    version='0.1.0',  # Change this version as needed
    author='Kriday Kini',  # Replace with your name
    author_email='kriday.kini@gmail.com',  # Replace with your email
    description='A simpler and more efficient way to use SQLite 3.',
    long_description=open('README.md').read(),  # Ensure you have a README.md file
    long_description_content_type='text/markdown',
    url='https://github.com/Pippoosh/better_sqlite',  # Replace with your GitHub repo URL
    packages=find_packages(),  # Automatically find packages in your project
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
    ],
    python_requires='>=3.12',  # Specify the Python version required
    install_requires=[],
)
