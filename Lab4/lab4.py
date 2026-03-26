num_tasks = int(input("Enter number of tasks: "))
tasks={}
for k in range(num_tasks):
    t_name = input("Enter task name: ")
    num_deps = int(input(f"How many dependencies for {t_name}? "))
    deps=[]
    for i in range(num_deps):
        dep=input(f"Enter dependency {i+1}: ")
        deps.append(dep)
    tasks[t_name]=deps
print("\nTASK STRUCTURE:")
for task, deps in tasks.items():
    print(f"{task} -> {deps}")

print("\nINITIAL TASKS (no dependencies):")
initial_tasks=[]
for task, deps in tasks.items():
    if len(deps)==0:
        initial_tasks.append(task)
        print(task)

if not initial_tasks:
    print("None")

e_order = []
completed_t = set()
while len(completed_t)<num_tasks:
    progress_made = False

    for task, deps in tasks.items():
        if task not in completed_t:
            all_d = True
            for d in deps:
                if d not in completed_t:
                    all_d = False
                    break

            if all_d:
                e_order.append(task)
                completed_t.add(task)
                progress_made = True

        
    if not progress_made:
            break        
    
print("\nEXECUTION ORDER:")
if len(e_order) == 0:
    print("No task can be started.")
else:
    for i in range(len(e_order)):
        print(f"Step {i+1}: {e_order[i]}")

if len(completed_t) == num_tasks:
    print("ALL TASKS COMPLETED SUCCESSFULLY")
else:
    print("ERROR: Circular dependency detected!")
    print("These tasks could not be completed:")
    for task in tasks:
        if task not in completed_t:
            print(task)