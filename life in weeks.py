#This is to calculate the number of weeks left in a persons life considering he/she might live till 90.
age = int(input("Enter Age: "))

#Max Age
total_age = 90

#Number of weeks till 90
tot_age_weeks = total_age * 52

#Number of weeks already completed
curr_in_weeks = age * 52

#Number of weeks remaining
remaining_weeks = tot_age_weeks - curr_in_weeks

#Printing using f-String
print(f"You have {remaining_weeks} of weeks left")
