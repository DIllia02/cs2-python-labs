import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from shared.student import GROUP_NAME, STUDENT_NAME, VARIANT_NUMBER
def main():
    print(f"Студент: {STUDENT_NAME} | Група: {GROUP_NAME} | Варіант: {VARIANT_NUMBER}\n")
    print("*Завдання 2*\n")

    users = {
        "cloud_architect": {
            "role": "cloud_security",
            "clearance": 4,
            "department": "Cloud",
            "active": True,
        },
        "devops_engineer": {
            "role": "devops",
            "clearance": 3,
            "department": "DevOps",
            "active": True,
        },
        "qa_tester": {
            "role": "quality_assurance",
            "clearance": 2,
            "department": "QA",
            "active": True,
        },
        "partner_access": {
            "role": "partner",
            "clearance": 2,
            "department": "Partnership",
            "active": True,
        },
        "migrated_user": {
            "role": "migrated",
            "clearance": 1,
            "department": "Migration",
            "active": False,
        },
    }

    resources = [
        ("cloud_configs", 4),
        ("deployment_pipelines", 3),
        ("test_environments", 2),
        ("partner_apis", 2),
        ("infrastructure_code", 4),
        ("shared_resources", 1),
        ("container_registry", 3),
        ("secrets_vault", 4),
        ("build_artifacts", 2),
        ("public_endpoints", 1),
    ]

    security_levels = (
        "Development",
        "Staging",
        "Production",
        "Critical Infrastructure",
    )
    blocked_users = {"migrated_user", "container_breach", "pipeline_compromise"}

    for resource_name, required_clearance in resources:
        level_name = security_levels[required_clearance - 1]
        print(f"Ресурс: {resource_name} | Необхідний рівень доступу: {level_name}")

    print()

    for username, user_info in users.items():
        for resource_name, required_clearance in resources:
            if username in blocked_users:
                status = "[!] DENY (User is blocked)"
            elif not user_info["active"]:
                status = "[!] DENY (User is inactive)"
            elif user_info["clearance"] < required_clearance:
                status = "[!] DENY (Access level too low)"
            else:
                status = "[+] ALLOW"

            print(
                f'| Користувач "{username}" | Ресурс: "{resource_name}" | Cтатус: {status} \n'
            )

if __name__ == "__main__":
    main()