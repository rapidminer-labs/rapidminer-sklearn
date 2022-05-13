import json
import os


def build_operator(path, name):
    operator_type = "learner"

    with open(os.path.join(path, name) + ".json", "r") as declaration_file:
        declaration = json.load(declaration_file)
    with open(os.path.join(path, name) + ".py", "r") as script_file:
        script = script_file.read()

    with open(os.path.join("rapidminer-sklearn", name + ".pyop"), "w") as outfile:
        json.dump({"type": operator_type, "declaration": declaration, "definition": script}, outfile)


if __name__ == "__main__":
    rootdir = "src"
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:

            if file.endswith(".json"):
                print("Building:", file.replace(".json", ""))
                build_operator(subdir, file.replace(".json", ""))
