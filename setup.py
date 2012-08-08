from setuptools import setup

setup(
    name = "decrypt",
    version = "0.1.0",
    description = "Pipe programs through decrypt to make your boss think you are l33t",
    author = "jtwaleson",
    url = "https://github.com/jtwaleson/decrypt",
    packages = ["decrypt"],
    zip_safe=False,
    entry_points = """
    [console_scripts]
    decrypt = decrypt:main
    """)

