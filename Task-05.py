class Interface:
    @classmethod
    def generate_interface(cls):
        print("\n"*50)
        print("Welcome to XYZ insurance company!")
        print("1) Add insurance company.\n2) Register Customer.\n3) View insurance companies and their insurances.")
        user_input=input("Enter the corresponding number to proceed: ")
        while user_input not in ['1','2','3']:
            user_input=input("Please enter 1,2 or 3 only.")
        if user_input=='1':
            print("\n" * 50)
            Insurance.create_insurance_obj()
            main_menu=input("Press M to go back to the main menu: ")
            if main_menu.lower()=='m':
                Interface.generate_interface()
        elif user_input=='2':
            print("\n" * 50)
            Customer.create_customer_obj()
            main_menu = input("Press M to go back to the main menu: ")
            if main_menu.lower() == 'm':
                Interface.generate_interface()
        elif user_input=='3':
            print("\n" * 50)
            Insurance.print_obj()
            main_menu = input("Press M to go back to the main menu: ")
            if main_menu.lower() == 'm':
                Interface.generate_interface()


class Insurance:
    list_insurance=[]
    dict_insurance={}
    def __init__(self,name_company,id_company):
        self.name_company=name_company
        self.id_company=id_company

    @classmethod
    def create_insurance_obj(cls):

        name_company=  input("Enter the company you wish to add:                                  ")
        id_company=    input("Enter the ID of company you added:                                  ")
        insurance_type=input("Enter the number of insurance type you want to add in this company: ")
        counter_insurance=1
        for insurances in range(int(insurance_type)):
            insurance_to_append=input("Enter insurance {}) ".format(counter_insurance))
            counter_insurance+=1
            Insurance.list_insurance.append(insurance_to_append)
            Insurance.dict_insurance[name_company.lower()]=Insurance.list_insurance
        Insurance.list_insurance=[]
        return(name_company,id_company)

    def print_obj():
        for company in Insurance.dict_insurance.keys():
            counterr=1
            print("-{}".format(company.title()))
        input_user=input("Select your required company: ")
        print("The available insurances for this company are listed below.")
        for insurances in Insurance.dict_insurance[input_user.lower()]:
            counterrr=1
            print(">{}".format(insurances))

class Customer:
    def __init__(self,name_cust,phoneno_cust,cnic_cust):
        self.name=   name_cust
        self.phoneno=phoneno_cust
        self.cnic=   cnic_cust

    @classmethod
    def create_customer_obj(cls):
        name_cust=   input("Enter the name of customer:         ")
        phoneno_cust=input("Enter the phone number of customer: ")
        cnic_cust=   input("Enter the cnic number of customer:  ")
        return cls(name_cust,phoneno_cust,cnic_cust)


Interface.generate_interface()




