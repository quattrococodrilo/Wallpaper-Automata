import setuptools

setuptools.setup(
    name='WallpaperAutomater',
    version='0.1',
    description='Sets automatically a wallpaper from Reddit.',
    author='Fernando Cruz',
    author_email='quattrococodrilo@gmail.com',
    licence='MIT',
    packages=setuptools.find_packages(),
    install_requires=[
        i.strip() for i in open('requirements.txt').readlines()

        if not i.startswith('#')
    ],
    entry_points={
        'console_scripts': [
            'wallpaper=bin.entry_point',
        ]
    }
)
