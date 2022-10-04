from tabulate import tabulate
import mysql.connector as mysql


def findByName(n):
    cs.execute("Select * from member_info where Member_Name='%s'" % n)
    t = cs.fetchall()
    nt = []
    for i in t:
        nt.append(i[:6])
    print(tabulate(nt, headers=['ID', 'Name', 'Age', 'Gender', 'Mobile', 'Activities']))


def findByPackageID(id):
    cs.execute("Select * from member_package_info where packageId=%s " % id)
    t = cs.fetchall()
    nt = []
    for i in t:
        nt.append(i)
    print(tabulate(nt, headers=['Package ID', 'ID', 'Special Package', 'Total Payment', 'Monthly Payment',
                                'End of Membership']))


def findByProgressID(id):
    cs.execute("Select * from progress_tracker where id ='%s'" % id)
    t = cs.fetchall()
    nt = []
    for i in t:
        nt.append(i)
    print(tabulate(nt, headers=['ID', 'Date', 'Weight', 'Height', 'BMI']))


conn = mysql.connect(host='localhost', user='root', password='neon@2004')
cs = conn.cursor()
cs.execute("create database if not exists Forger_gym")
cs.execute("use Forger_gym")
cs.execute(
    'create table if not exists Member_Info(id int(10) primary key not null auto_increment,Member_Name varchar(30),age int,'
    'gender char(1),mobile int,Activities varchar(40),password varchar(20))')
cs.execute(
    "create table if not exists Member_package_info(packageId int primary key auto_increment, id int(10),special_package varchar(40),total_payment int," +
    "monthly_payment int,end_of_membership date,constraint foreign key(id) references Member_Info(id) on delete " +
    "cascade)")
cs.execute(
    "create table if not exists progress_tracker(id int, date date,weight decimal(5,2),height decimal(5,2),bmi int," +
    'constraint foreign key(id) references Member_Info(id) on delete cascade)')


class bgc:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    WHITE = '\033[37m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    BLACK = '\033[30m'


def ADMIN():
    password = input('Enter your password: ' + bgc.ENDC)
    if password == '123456':
        while True:
            print(bgc.BOLD + '''MENU:
            1.Add new member.
            2.Show all members.
            3.Delete a member.
            4.Update a member.
            5.Search a member.
            6.Add new package.
            7.Show all packages.
            8.Delete a package.
            9.Update a package.
            10.Search a package.
            11.Add new progress.
            12.Show all progress.
            13.Delete a progress.
            14.Update a progress.
            15.Search a progress.
            16.Exit'''.format(bgc.BOLD))
            choice = int(input('Enter your choice: ' + bgc.ENDC))

            if choice == 1:
                name = input('Enter Name: ' + bgc.ENDC)
                age = int(input('Enter Age: ' + bgc.ENDC))
                gender = input('Enter Gender: ' + bgc.ENDC)
                mobile = int(input('Enter Mobile Number: ' + bgc.ENDC))
                activities = input('Enter Activities: ' + bgc.ENDC)
                password = input('Enter Password: ' + bgc.ENDC)
                cs.execute(
                    "insert into Member_Info(Member_Name, Age, Gender, Mobile, Activities, Password) VALUES('%s',%s,'%s',%s,'%s','%s')" % (
                        name, age, gender, mobile, activities, password))
                conn.commit()
                print(bgc.OKGREEN + 'Details Inserted' + bgc.ENDC)

            elif choice == 2:
                cs.execute('select * from Member_Info')
                hold = cs.fetchall()
                nt = []
                for i in hold:
                    nt.append(i[:6])
                print(tabulate(nt, headers=['ID', 'Name', 'Age', 'Gender', 'Mobile', 'Activities']))

            elif choice == 3:
                id = int(input('Enter ID: ' + bgc.ENDC))
                cs.execute("delete from Member_Info where id=%s" % id)
                conn.commit()
                print(bgc.OKGREEN + 'Member Deleted' + bgc.ENDC)

            elif choice == 4:
                id = int(input('Enter ID: ' + bgc.ENDC))
                name = input('Enter Name: ' + bgc.ENDC)
                age = int(input('Enter Age: ' + bgc.ENDC))
                gender = input('Enter gender: ' + bgc.ENDC)
                mobile = int(input('Enter Mobile Number: ' + bgc.ENDC))
                activities = input('Enter Activities: ' + bgc.ENDC)
                password = input('Enter Password: ' + bgc.ENDC)
                cs.execute("update Member_Info set Member_Name = '%s', age = '%s',"
                           "gender = '%s', mobile = '%s', Activities = '%s', password = '%s' where id = %s" % (
                               name, age, gender, mobile, activities, password, id))
                conn.commit()
                print(bgc.OKGREEN + 'Details Updated' + bgc.ENDC)

            elif choice == 5:
                name = input('Enter Name: ' + bgc.ENDC)
                findByName(name)

            elif choice == 6:
                id = int(input('Enter Member ID: ' + bgc.ENDC))
                special_package = input('Enter Special Package: ' + bgc.ENDC)
                total_payment = int(input('Enter Total Payment: ' + bgc.ENDC))
                monthly_payment = int(input('Enter Monthly Payment: ' + bgc.ENDC))
                end_of_membership = input('Enter End of Membership: ' + bgc.ENDC)
                cs.execute(
                    "insert into Member_package_info(id, special_package, total_payment, monthly_payment, end_of_membership) VALUES(%s,'%s',%s,%s,'%s')" % (
                        id, special_package, total_payment, monthly_payment, end_of_membership))
                conn.commit()
                print(bgc.OKGREEN + 'Package Added' + bgc.ENDC)

            elif choice == 7:
                cs.execute('select * from Member_package_info')
                hold = cs.fetchall()
                nt = []
                for i in hold:
                    nt.append(i[:6])
                print(tabulate(nt, headers=['Package ID', 'Member ID', 'Special Package', 'Total Payment',
                                            'Monthly Payment', 'End of Membership']))

            elif choice == 8:
                id = int(input('Enter Package ID: ' + bgc.ENDC))
                cs.execute("delete from Member_package_info where id=%s" % id)
                conn.commit()
                print(bgc.OKGREEN + 'Package Deleted' + bgc.ENDC)

            elif choice == 9:
                id = int(input('Enter Package ID: ' + bgc.ENDC))
                special_package = input('Enter Special Package: ' + bgc.ENDC)
                total_payment = int(input('Enter Total Payment: ' + bgc.ENDC))
                monthly_payment = int(input('Enter Monthly Payment: ' + bgc.ENDC))
                end_of_membership = input('Enter End of Membership: ' + bgc.ENDC)
                cs.execute("update Member_package_info set special_package = '%s', total_payment = '%s',"
                           "monthly_payment = '%s', end_of_membership = '%s' where id = %s" % (
                               special_package, total_payment, monthly_payment, end_of_membership, id))
                conn.commit()
                print(bgc.OKGREEN + 'Package Updated' + bgc.ENDC)

            elif choice == 10:
                id = int(input('Enter Package ID: ' + bgc.ENDC))
                findByPackageID(id)

            elif choice == 11:
                id = int(input('Enter Member ID: ' + bgc.ENDC))
                date = input('Enter Date: ' + bgc.ENDC)
                weight = float(input('Enter Weight in Kg: ' + bgc.ENDC))
                height = float(input('Enter Height in metres: ' + bgc.ENDC))
                bmi = weight // (height * height)
                cs.execute("insert into progress_tracker(id,date, weight, height, bmi) VALUES(%s,'%s',%s,%s,%s)" % (
                    id, date, weight, height, bmi))
                conn.commit()
                print(bgc.OKGREEN + 'Progress Added' + bgc.ENDC)

            elif choice == 12:
                cs.execute('select * from progress_tracker')
                hold = cs.fetchall()
                nt = []
                for i in hold:
                    nt.append(i[:5])
                print(tabulate(nt, headers=['Member ID', 'Date', 'Weight', 'Height', 'BMI']))

            elif choice == 13:
                id = int(input('Enter Member ID: ' + bgc.ENDC))
                cs.execute("delete from progress_tracker where id=%s" % id)
                conn.commit()
                print(bgc.OKGREEN + 'Progress Deleted' + bgc.ENDC)

            elif choice == 14:
                id = int(input('Enter Member ID: ' + bgc.ENDC))
                weight = float(input('Enter Weight: ' + bgc.ENDC))
                height = float(input('Enter Height: ' + bgc.ENDC))
                bmi = weight // (height * height)
                cs.execute("update progress_tracker set weight = '%s', height = '%s',"
                           "bmi = '%s' where id = %s" % (
                               weight, height, bmi, id))
                conn.commit()
                print(bgc.OKGREEN + 'Progress Updated' + bgc.ENDC)

            elif choice == 15:
                id = int(input('Enter Member ID: ' + bgc.ENDC))
                findByProgressID(id)

            elif choice == 16:
                break

            else:
                print(bgc.FAIL + 'Invalid Choice' + bgc.ENDC)


def MEMBER():
    while True:
        print('''MENU:
1. Login.
2. Exit.'''.format(bgc.BOLD))
        choice = int(input('Enter choice: ' + bgc.ENDC))
        if choice == 1:
            mobile = input("Enter your mobile: ")
            password = input("Enter your password: ")
            cs.execute(
                "SELECT id, mobile, password from member_info WHERE mobile = %s AND password = '%s'" % (
                    mobile, password))
            t = cs.fetchall()
            if len(t) > 0:
                print("Login successful")
                userId = t[0][0]
                while True:
                    print(bgc.OKBLUE + '''
1. View Profile
2. Edit Profile
3. View Package
4. View Progress
5. Edit Progress
6. Exit
''' + bgc.ENDC)
                    choice = int(input('Enter Choice: ' + bgc.ENDC))

                    if choice == 1:
                        cs.execute('select * from Member_Info where id=%s' % userId)
                        hold = cs.fetchall()
                        nt = []
                        for i in hold:
                            nt.append(i[:7])
                        print(tabulate(nt, headers=['Member ID', 'Name', 'Age', 'Gender', 'Mobile', 'Activities',
                                                    'Password']))

                    elif choice == 2:
                        name = input('Enter Name: ' + bgc.ENDC)
                        age = int(input('Enter Age: ' + bgc.ENDC))
                        gender = input('Enter Gender: ' + bgc.ENDC)
                        mobile = input('Enter Mobile: ' + bgc.ENDC)
                        activities = input('Enter Activities: ' + bgc.ENDC)
                        password = input('Enter Password: ' + bgc.ENDC)
                        cs.execute(
                            "update Member_Info set Member_Name = '%s', age = %s,gender = '%s', mobile = %s, Activities = '%s', password = '%s' where id = %s" % (
                                name, age, gender, mobile, activities, password, userId))
                        conn.commit()
                        print(bgc.OKGREEN + 'Profile Updated' + bgc.ENDC)

                    elif choice == 3:
                        cs.execute('select * from Member_package_info where id=%s' % userId)
                        hold = cs.fetchall()
                        nt = []
                        for i in hold:
                            nt.append(i[:6])
                        print(tabulate(nt, headers=['Package ID', 'Member ID', 'Special Package', 'Total Payment',
                                                    'Monthly Payment', 'End of Membership']))

                    elif choice == 4:
                        cs.execute('select * from progress_tracker where id=%s' % userId)
                        hold = cs.fetchall()
                        nt = []
                        for i in hold:
                            nt.append(i[:5])
                        print(tabulate(nt, headers=['Progress ID', 'Member ID', 'Weight', 'Height', 'BMI']))

                    elif choice == 5:
                        weight = float(input('Enter Weight: ' + bgc.ENDC))
                        height = float(input('Enter Height: ' + bgc.ENDC))
                        bmi = weight // (height * height)
                        cs.execute("update progress_tracker set weight = %s, height = %s,"
                                   "bmi = %s where id = %s" % (
                                       weight, height, bmi, userId))
                        conn.commit()
                        print(bgc.OKGREEN + 'Progress Updated' + bgc.ENDC)

                    elif choice == 6:
                        break

                    else:
                        print(bgc.FAIL + 'Invalid Choice' + bgc.ENDC)

            else:
                print(bgc.FAIL + "Login failed" + bgc.ENDC)

        elif choice == 2:
            break

        else:
            print(bgc.FAIL + 'Invalid Choice' + bgc.ENDC)


while True:
    print("WELCOME TO Forger Gym" + bgc.BOLD + bgc.UNDERLINE)
    login = int(input('''Login:
1. Admin
2. Member
3. Exit

Enter your choice:'''.format(bgc.BOLD)))
    if login == 1:
        ADMIN()
    elif login == 2:
        MEMBER()
    elif login == 3:
        break
    else:
        print(bgc.FAIL + 'Invalid Choice' + bgc.ENDC)