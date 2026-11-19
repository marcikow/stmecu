import json
from pathlib import Path

def load_profile_data():
    with open(CALIBRATION_DIR, "r") as f:
        data = json.load(f)
    return data

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CALIBRATION_DIR = PROJECT_ROOT / "calibration" / "profiles.jason"


def validate_map(data, profile_name, map_name):
    current_map = data["profiles"][profile_name]["maps"][map_name]

    rpm = current_map["axes"]["RPM"]
    tps = current_map["axes"]["TPS"]
    values = current_map["values"]
    
    if len(rpm) != len(tps):
        raise ValueError("RPM and TPS arrays must have the same length")

    for row in values:
        if len(row) != len(tps):
            raise ValueError("Each row in values must have the same length as RPM array")
    
    print(f"All validations for {profile_name} passed")
    return True



if __name__ == "__main__":
    profiles_data = load_profile_data()

    print("version:", profiles_data["version"])
    print("Cylinders count:", profiles_data["engine_info"]["cylinders"])
    print("profiles names:", list(profiles_data["profiles"]))
    for profile_name, profile in profiles_data["profiles"].items():
        for map_name in profile["maps"]:
            validate_map(profiles_data, profile_name, map_name)


