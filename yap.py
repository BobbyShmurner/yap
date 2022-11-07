import requests

from setuptools._vendor.packaging import tags, version

def install(package: str, version: str = "*"):
    print(f"Installing Package \"{package.title()}\"...")

    response = requests.get(f"https://pypi.org/pypi/{package}/json")
    content = str(response.content)

    for tag in tags.sys_tags():
        if str(tag) in content:
            print(f"Found compatible wheel \"{tag}\"!")
            break
        else:
            print(f"No wheel for tag \"{tag}\"")