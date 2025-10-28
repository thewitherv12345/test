import subprocess  

def run_git_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return result.stdout.strip()
    except:
        print("Error")
        exit(1) 
        
status_output = run_git_command("git status --porcelain")

changed_files = [line for line in status_output.splitlines() if line.startswith((' M', '??', ' A'))]  
num_changed = len(changed_files)

commit_message = f"{num_changed} files changed"

run_git_command("git add .")

run_git_command(f'git commit -m "{commit_message}"')

run_git_command("git push origin main")  

print("Success")