import subprocess  # Для выполнения команд Git

def run_git_command(command):
    """Функция для выполнения Git-команды и обработки ошибок."""
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении команды '{command}': {e.stderr.strip()}")
        exit(1)  # Выходим из скрипта при ошибке

# Шаг 1: Получаем статус Git, чтобы найти изменённые файлы
status_output = run_git_command("git status --porcelain")

# Шаг 2: Считаем количество изменённых файлов
# --porcelain даёт формат вроде " M file.txt" (M - modified, ?? - new)
changed_files = [line for line in status_output.splitlines() if line.startswith((' M', '??', ' A'))]  # M: modified, ??/A: added/new
num_changed = len(changed_files)

# Шаг 3: Формируем сообщение коммита с количеством файлов (уникальная фича для варианта 8)
commit_message = f"Automated commit: {num_changed} files changed"
print(f"Сообщение коммита: {commit_message}")

# Шаг 4: Добавляем все изменения (git add .)
print("Выполняем git add .")
run_git_command("git add .")

# Шаг 5: Делаем коммит
print("Выполняем git commit.")
run_git_command(f'git commit -m "{commit_message}"')

# Шаг 6: Пушим в удалённый репозиторий (по умолчанию origin main; измени на master если нужно)
print("Выполняем git push.")
run_git_command("git push origin main")  # Если ветка master, измени на "git push origin master"

print("Успех! Коммит и пуш завершены.")