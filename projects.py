import date_validation
import ast


def projects_menu():
    print("""
    1-Create new project
    2-View all projects
    3-Edit your projects
    4-Delete your projects
    5-Search projects by date
    """)


class Project:
    def __init__(self, email, title, details, target, start, end):
        self.email = email
        self.title = title
        self.details = details
        self.target = target
        self.start = start
        self.end = end

    @classmethod
    def create(cls, email):
        title = input("Please enter project title : ")
        while not title.isalnum():
            print("sorry title can contain characters or numbers only!")
            title = input("Please enter project title : ")
        details = input("Please enter project details : ")
        total_target = input("please enter your project target : ")
        while not total_target.isdecimal():
            print("Target must be digits only!")
            total_target = input("please enter your project target : ")
        start_time = input("please enter your project start date as (Year-Month-Day) : ")
        while not date_validation.check_date(start_time):
            print("Please enter a valid date as shown !")
            start_time = input("please enter your project start date as (Year-Month-Day) : ")
            date_validation.check_date(start_time)
        end_time = input("please enter your project end date as (Year-Month-Day) : ")
        while not date_validation.check_date(end_time):
            print("Please enter a valid date as shown !")
            end_time = input("please enter your project end date as (Year-Month-Day) : ")
            date_validation.check_date(end_time)
        while not date_validation.date_compare(start_time, end_time):
            print("End date must be after start date !")
            end_time = input("please enter your project end date as (Year-Month-Day) : ")
            date_validation.check_date(end_time)
            date_validation.date_compare(start_time, end_time)

        return cls(email, title, details, total_target, start_time, end_time)

    @staticmethod
    def edit(email, title):
        projects_data = open("projects.txt", "r+")
        lines = projects_data.readlines()
        for index, line in enumerate(lines):
            project = ast.literal_eval(line)
            if project["owner"] == email and project["title"] == title:
                project = Project.create(email)
                project_data = {
                    'owner': project.email,
                    'title': project.title,
                    'details': project.details,
                    'total_target': project.target,
                    'start_date': project.start,
                    'end_date': project.end
                }
                lines[index] = str(project_data) + '\n'
                projects_data.truncate(0)
                projects_data.seek(0)
                projects_data.writelines(lines)
                print("Your project edited successfully")
                break
            elif project["title"] == title and project["owner"] != email:
                print("This project belong to another user , sorry you can edit in your projects only!")
                break
        else:
            print("There is no project with this title!")

    @staticmethod
    def view():
        project_arr = []
        projects_data = open("projects.txt", "r")
        lines = projects_data.readlines()
        for line in lines:
            project = ast.literal_eval(line)
            project_arr.append(project)

        return project_arr

    @staticmethod
    def delete(email, title):
        projects_data = open("projects.txt", "r+")
        lines = projects_data.readlines()
        for index, line in enumerate(lines):
            project = ast.literal_eval(line)
            if project["owner"] == email and project["title"] == title:
                lines.pop(index)
                projects_data.truncate(0)
                projects_data.seek(0)
                projects_data.writelines(lines)
                print("Your project deleted successfully")
                break
            elif project["title"] == title and project["owner"] != email:
                print("This project belong to another user , sorry you can delete your projects only!")
                break
        else:
            print("There is no project with this title!")

    @staticmethod
    def search():
        date = input("please enter project date as (Year-Month-Day) : ")
        while not date_validation.check_date(date):
            print("Please enter a valid date as shown !")
            date = input("please enter project date as (Year-Month-Day) : ")
            date_validation.check_date(date)

        array = []
        projects_data = open("projects.txt", "r")
        lines = projects_data.readlines()
        for line in lines:
            project = ast.literal_eval(line)
            if project['start_date'] == date:
                array.append(project)

        if len(array) > 0:
            return array
        else:
            print("There is no project with this date .")
            Project.search()

    @staticmethod
    def projects_actions(email):
        projects_menu()
        selection = int(input("Choose an action : "))
        if selection == 1:
            project = Project.create(email)
            project_data = {
                'owner': project.email,
                'title': project.title,
                'details': project.details,
                'total_target': project.target,
                'start_date': project.start,
                'end_date': project.end
            }
            projects_file = open("projects.txt", "a")
            projects_file.write(str(project_data) + '\n')
            projects_file.close()
            print("Thank you , your project added successfully :)")
            Project.projects_actions(email)

        elif selection == 2:
            projects = Project.view()
            for index, value in enumerate(projects):
                print(index+1, "-", value)
            Project.projects_actions(email)

        elif selection == 3:
            title = input("please enter title of project to edit : ")
            Project.edit(email, title)
            Project.projects_actions(email)

        elif selection == 4:
            title = input("please enter title of project to delete : ")
            Project.delete(email, title)
            Project.projects_actions(email)

        elif selection == 5:
            data = Project.search()
            for index, project in enumerate(data):
                print(index+1, "-", project)
            Project.projects_actions(email)

        else:
            print("please enter valid option!")
            Project.projects_actions(email)
