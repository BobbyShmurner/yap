import os

IS_IN_SCHOOL = os.path.exists("N:\\")
USE_SUBPROCESS = True

USERNAME = os.environ['USERNAME']
ENV_PATH = "N:\\Python\\Environment" if IS_IN_SCHOOL else os.path.abspath('./env')