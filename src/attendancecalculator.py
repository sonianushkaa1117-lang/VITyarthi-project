#code to calculate attendance
def attendance():
    type=int(input("Select existing attendance(1) or attendance prediction(2)"))
    if type==1:
        sub=int(input("English(1),other subjects(2)"))
        total_1=26                                                              #a total of 26 classes per subject(excluding english) are taken per sem
        total_2=10                                                              #a total of 10 classes of english are taken per sem
        if sub==1:
            eng=int(input("How many classes did you attend in the sub?"))
            if eng<=10:
                attendance_eng=(eng/total_2)*100
                print(attendance_eng)
            else:
                print("Invalid input")
        elif(sub==2):
            num_classes=int(input("How many classes did you attend in the sub?"))
            if num_classes<=26:
                attendance=(num_classes/total_1)*100
                print(attendance)
            else:
                print("invalid input")
    if type==(2):
        type_1=int(input("Find attendance for provided no. of classes(1) or Find no. of classes for provided percentage(2)"))
        if type_1==1:
            sub=int(input("subject:english(1),other sub(2):"))
            if sub==1:
                num1=int(input("Enter no of classes you wish to take out of 10"))
                percent_attendance=(num1/10)*100
            if sub!=1:
                num2=int(input("Enter no of classes you wish to take out of 26"))
                percent_attendance=(num2/26)*100
            print(percent_attendance)
        if type_1==2:
            sub=int(input("Enter subject:english(1),other(2):"))
            if sub==1:
                num_3=int(input("Enter the percentage you want to maintain"))
                class1=num_3//10
            if sub!=1:
                num_4=int(input("Enter the percentage you want to maintain"))
                class1=num_4*26//100
            print(class1)

attendance()
