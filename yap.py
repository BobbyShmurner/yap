from setuptools._vendor.packaging import tags, version

def install(package: str, version: str = "*"):
    print(f"Installing Package \"{package.title()}\"...")