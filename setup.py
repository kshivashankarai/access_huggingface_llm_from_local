from setuptools import find_packages,setup

setup(
    name='access_huggingface_llm_from_local',
    version='0.0.1',
    author='shiva shankar',
    author_email='kshivashankarai',
    install_requires=["llama-cpp-python","huggingface-hub","accelerate","peft","bitsandbytes","transformers","trl",],
    packages=find_packages()
)