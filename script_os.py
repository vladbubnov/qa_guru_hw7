import os.path

CURRENT_FILE = os.path.abspath(__file__)
print(CURRENT_FILE)

CURRENT_DIR = os.path.dirname(CURRENT_FILE)
print(CURRENT_DIR)

RESOURCES_DIR = os.path.join(CURRENT_DIR, "resources")
print(RESOURCES_DIR)

# if not os.path.exists("temp"):
#     os.mkdir("temp")
