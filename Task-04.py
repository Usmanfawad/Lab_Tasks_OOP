class Cs:
    dict_courses_cs={}
    dict_courses_se={}

    def __init__(self,university_name,university_id):
        self.uni_name=university_name
        self.uni_id  =university_id

    def interface():
        print("\n"*40)
        print("1) Add CS courses.\n2) Add SE courses.\n3) View all Cs courses.\n4) View all Se courses.")
        user_input=input("Enter the corresponding number to proceed: ")
        while user_input not in ['1','2','3','4']:
            user_input=input("Enter 1 or 2 only: ")

        if user_input=='1':
            print("\n" * 40)
            cs.create_cs_obj()
            back_to_main=input("Enter >M< to go back to the main menu: ")
            if back_to_main.lower()=='m':
                Cs.interface()
        elif user_input=='2':
            print("\n" * 40)
            se.create_se_obj()
            back_to_main = input("Enter >M< to go back to the main menu: ")
            if back_to_main.lower() == 'm':
                Cs.interface()
        elif user_input=='3':
            print("\n" * 40)
            if Cs.dict_courses_cs=={}:
                print("No courses added yet.")
            else:
                counter_cs=1
                for code,course in Cs.dict_courses_cs.items():
                    print("{}) {} :{:<20}".format(counter_cs,code,course))
                    counter_cs+=1
            back_to_main = input("Enter >M< to go back to the main menu: ")
            if back_to_main.lower() == 'm':
                Cs.interface()

        elif user_input=='4':
            print("\n" * 40)
            if Cs.dict_courses_se=={}:
                print("No courses added yet.")
            else:
                counter_cs=1
                for code,course in Cs.dict_courses_se.items():
                    print("{}) {} :{:<20}".format(counter_cs,code,course))
                    counter_cs+=1
            back_to_main = input("Enter >M< to go back to the main menu: ")
            if back_to_main.lower() == 'm':
                Cs.interface()

class cs:
    def __init__(self,course_name,course_code):
        self.course_name=course_name
        self.course_code=course_code

    @classmethod
    def create_cs_obj(cls):
        course_name=input("Enter course name: ")
        course_code=input("Enter course code: ")
        Cs.dict_courses_cs[course_code]=course_name
        return cls(course_name,course_code)

class se:
    def __init__(self,coursename,coursecode):
        self.coursename=coursename
        self.coursecode=coursecode

    @classmethod
    def create_se_obj(cls):
        coursename=input("Enter course name: ")
        coursecode=input("Enter course code: ")
        Cs.dict_courses_se[coursecode]=coursename
        return cls(coursename,coursecode)

uni= Cs("UIT","1001")
Cs.interface()