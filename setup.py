from setuptools import setup, find_packages

setup(
    name='uber-fare-prediction',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
        'seaborn',
        'scikit-learn',
        'xgboost',
    ],
    entry_points={
        'console_scripts': [
            'run_preprocessing=scripts.data_preprocessing:main',
            'run_eda=scripts.eda:main',
            'run_training=scripts.model_training:main',
            'run_evaluation=scripts.model_evaluation:main',
        ],
    },
)
