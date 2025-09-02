import os
import shutil

# Updated list of paths to generated files and folders
generated_paths = [
    "phases/phase1_concept_strategy/output/",
    "phases/phase2_development_planning/deliverables/generated_files/",
    "phases/phase3_ai_execution/codebase/build/",
    "phases/phase4_testing_iteration/tests/test_results/",
    "phases/phase5_launch_growth/marketing/marketing_materials/",
]

def reset_project():
    """Deletes all generated files and folders to reset the project."""
    for path in generated_paths:
        if os.path.exists(path):
            if os.path.isdir(path):
                shutil.rmtree(path)
                print(f"Deleted folder: {path}")
            else:
                os.remove(path)
                print(f"Deleted file: {path}")
    print("Project reset successfully!")

if __name__ == "__main__":
    confirm = input("Are you sure you want to reset the project? This will delete all generated files. (yes/no): ")
    if confirm.lower() == "yes":
        reset_project()
    else:
        print("Reset canceled.")
