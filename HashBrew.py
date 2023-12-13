import time
import os
import random
from github import Github
from git import Repo

inp = ""
interg = ""
original_repo_url = "https://github.com/PuppyStudios1/HashBrew-Cloud.git"
branchname = ""
name = ""
email = ""
pkgname = ""
pkgcontent = ""
locate = ""
# Before Defines
def find_and_clone_file(repo_url, filename):
  """
  Searches a GitHub repository for a specific file and clones it.

  Args:
    repo_url: The URL of the GitHub repository.
    filename: The name of the file to search for.
  """

  # Get the GitHub repository object.
  github = Github()
  repo = github.get_repo(repo_url)

  # Search for the file.
  for content in repo.get_contents(""):
    if content.name == filename:
      # If the file is found, clone it.
      download_url = content.download_url
      os.system(f"curl -L {download_url} -o {filename}")
      print(f"File '{filename}' downloaded successfully.")
      return

  # If the file is not found, raise an error.
  raise FileNotFoundError(f"File '{filename}' not found in repository.")

# Program starts here!
print("\n Welcome to HashBrew! v1.1 \n")
print("HashBrew Package Manager Enviroment (HPME)")
print("Loading enviroment... \n")
time.sleep(3)

if __name__ == "__main__":          # <- Hash engine
    while True:
        inp = input("HashBrew@pkg:~$ ")

        if inp == "Hash":
            print("`Hash` command used externaly.")

        if inp == "Hash Intergrate":
            interg = input("Enter Intergration ID: ")

        if inp == "Hash.Brewer":
            pkgname = input("Enter Package name: ")
            pkgcontent = input("Enter contents: ")

            with open(os.path.join(os.getcwd(), pkgname), "w") as f:
                f.write(pkgcontent)

            print(f"Created package: {pkgname}")

            # Clone the original repository
            os.system(f"git clone {original_repo_url}")

            # Move to the cloned repository
            os.chdir(os.path.join(os.getcwd(), "original_repo_name"))

            # Create a new branch for your changes
            branchname = input("what would you like for your branch name?: ")
            os.system(f"git checkout -b " + branchname)

            # Copy the created package to the appropriate location
            os.system(f"cp ../{pkgname} .")

            # Add the copied file to staging area
            os.system(f"git add {pkgname}")

            email = input("Enter your email for the commit: ")
            name = input ("enter your name for the commit: ")
            # Set your email and name for commit
            os.system("git config --global user.email "+ email)
            os.system("git config --global user.name "+ name)

            # Commit the changes with a message
            os.system(f"git commit -m 'Added {pkgname} to your branch'")

            # Push the changes to your forked repository
            os.system("git remote add fork https://github.com/PuppyStudios1/HashBrew-Cloud.git")
            os.system("git push -u fork "+ branchname)

            print(f"Package pushed to your forked repository: https://github.com/PuppyStudios1/HashBrew-Cloud.git")

            def generate_unique_random_number_string(num_digits):
                # Generate a random number with the specified number of digits.
                random_number = random.randint(10**(num_digits-1), 10**num_digits-1)
                # Convert the random number to a string and return it.
                random_number_string = str(random_number)
                # Check if the random number string is unique and has the correct number of digits.
                if len(random_number_string) == num_digits:
                    return random_number_string

            # Generate a unique random number string with 5 digits.
            unique_number_string = generate_unique_random_number_string(5)
            
            generate_unique_random_number_string

            print ("Your Package ID is: "+ unique_number_string)

        if inp == "clear":
            os.system("clear")

        if inp == "Hash inst pkgutil":
            locate = input ("input cloud pkg directory: ")
            os.system("git clone https://github.com/PuppyStudios1/HashBrew-Cloud.git "+ locate)

        if inp == "Hash install":
            pkginstall = input("what to install?: ")

            try:
                find_and_clone_file(original_repo_url, pkginstall)
            except FileNotFoundError as e:
                print(e)

