import shutil
import os

def create_submission_zip():

    project_folder = "C:/Users/karti/OneDrive/Desktop/Project Prototype"
    output_zip = "submission.zip"

    shutil.make_archive("submission", 'zip', project_folder)
    print("✅ Project successfully compressed into submission.zip!")

if __name__ == "__main__":
    create_submission_zip()
