import setuptools

setuptools.setup(
    name='Speech-speech-to-sign-language-converter',
    version='0.1.0',
    description='Python project',
    author='Shrinivas Kulkarni',
    author_email='kulkarnishrinivas66@gmail.com',
    url='https://github.com/Shrini66/BE_Project',
    packages=setuptools.find_packages(),
    setup_requires=['nltk', 'joblib','click','regex','sqlparse','setuptools'],
)