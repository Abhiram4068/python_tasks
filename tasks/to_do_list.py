def to_do_list():
    tasks=[]
    while True:
        print("Enter your choice:")
        print("1-Add task")
        print("2-View tasks")
        print("3-Remove tasks")
        print("4-Exit")
        user_choice=int(input("Enter your choice:"))
        if user_choice==1:
            print("ADD YOUR TASK.")
            task=input("Enter your task:")
            tasks.append(task)
            print("TASK ADDED!")
        elif user_choice==2:
            print("YOUR TASKS:")
            i = 1
            for task in tasks:
                print(i,task)
                i+=1
        elif user_choice==3:
            task=input("Enter the task to be removed:")
            if task in tasks:
                tasks.remove(task)
                print("TASK REMOVED!")
            else:
                print("Task not found.")
        elif user_choice==4:
            print("Exiting....")
        else:
            print("Invalid input!")
        exit_choice=input("Do you want to continue?(y/n)").lower()
        if exit_choice!="y":
            print("Exiting....")
            break
to_do_list()