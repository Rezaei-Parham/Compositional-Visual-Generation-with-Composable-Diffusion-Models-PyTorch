from setuptools import setup

setup(
    name="composable-diffusion",
    packages=[
        "composable_diffusion",
        "composable_diffusion.clip",
        "composable_diffusion.tokenizer",
        "composable_diffusion.composable_stable_diffusion",
        "point_e",
        "point_e.diffusion",
        "point_e.evals",
        "point_e.models",
        "point_e.util",
    ],
    package_data={
        "composable_diffusion.tokenizer": [
            "bpe_simple_vocab_16e6.txt.gz",
            "encoder.json.gz",
            "vocab.bpe.gz",
        ],
        "composable_diffusion.clip": ["config.yaml"],
    },
    install_requires=[
        "Pillow",
        "attrs",
        "torch",
        "filelock",
        "requests",
        "tqdm",
        "ftfy",
        "regex",
        "numpy",
        "blobfile",
        "torchvision",
        "diffuser",
        "transformers",
        "filelock",
        "fire",
        "humanize",
        "requests",
        "tqdm",
        "matplotlib",
        "scikit-image",
        "scipy",
        "clip @ git+https://github.com/openai/CLIP.git",
        "open3d"
    ],
    author="nanliu",
    version='3.0',
)
