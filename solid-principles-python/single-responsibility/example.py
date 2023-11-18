class Project:
    def __init__(self, name: str):
        self.name = name

class Developer:
    def __init__(self, name: str, programming_languages: list, projects: list):
        self.name = name
        self.programming_languages = programming_languages
        self.projects = [Project(project_name) for project_name in projects]

class Manager:
    def __init__(self, name: str, projects: list):
        self.name = name
        self.projects = [Project(project_name) for project_name in projects]

class Tester:
    def __init__(self, name: str):
        self.name = name

    def test_code(self, developer: Developer):
        print(f"{self.name} is testing code written by {developer.name}")

class CodeWriter:
    def __init__(self, developer: Developer):
        self.developer = developer

    def write_code(self):
        print(f"Writing code by {self.developer.name}")

class CodeTester:
    def __init__(self, tester: Tester):
        self.tester = tester

    def test_code(self, developer: Developer):
        print(f"Testing code written by {developer.name}")

class ProjectManager:
    def __init__(self, manager: Manager, active_project_name: str):
        self.manager = manager
        self.active_project_name = active_project_name

    def project_manage(self):
        print(f"{self.active_project_name} project managing by {self.manager.name}")

if __name__ == '__main__':
    developer = Developer("Alican", ["Python", "C#"], ["Project1", "Project2"])
    code_writer = CodeWriter(developer)
    code_writer.write_code()
    tester = Tester("Hakan")
    tester.test_code(developer)
    manager = Manager("Uğur", ["Project1", "Project2"])
    active_project_name = "Project1" 
    project_manager = ProjectManager(manager, active_project_name)
    project_manager.project_manage()

