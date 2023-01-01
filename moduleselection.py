import pandas as pd

print("1.Creating a student database.")
print("2.View Batch database.")
print("3.View Course database.")
print("4.View Departments database.")
a = int(input("Enter the module number you want to open: "))
if a==1:
    import stdmanagement
    exec('stdmanagement.py')
elif a==2:
    df = pd.read_csv('Batch.csv')

    print(df)
elif a==3:
    df = pd.read_csv('Course.csv')

    print(df)
elif a==4:
    df = pd.read_csv('Department.csv')

    print(df)

# elif a==2:
#     exec('Batch.csv')
# elif a==3:
#     exec('Course.csv')
# elif a==4:
#     exec('Department.csv')