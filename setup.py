from setuptools import setup

setup(
    name='transcriptic',
    description='Transcriptic CLI & Python Client Library',
    url='https://github.com/transcriptic/transcriptic',
    version='2.0.3',
    packages=['transcriptic', 'transcriptic.analysis'],
    install_requires=[
        'Click>=5.1',
        'requests',
        'autoprotocol'
    ],
    entry_points='''
        [console_scripts]
        transcriptic=transcriptic.cli:cli
    '''
)
