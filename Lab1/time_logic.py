total_seconds = int(input("Enter a total number of seconds: "))
hours = total_seconds//3600
remaining = total_seconds%3600
minutes = remaining//60
seconds = remaining%60

print(total_seconds, "seconds is", hours, "hours,", minutes, "minutes, and", seconds, "seconds.")