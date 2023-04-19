import pandas as pd

presReadingList=[]
#ask for sensors' pressure data from user to Data Sensor 1 and keep in dataSensor1.txt
def dataSensor1():
    print("-----Data Sensor 1-----\n")
    file1="dataSensor1.txt"
    outfile=open(file1,"w")
    outfile.write("SensorID,City,PressureReading")
    response=''
    while response.upper()!="Q":
        outfile.write("\n")
        sensorID=int(input("Sensor ID: "))
        city=str(input("City: "))
        presReading=eval(input("Pressure Reading: "))
        presReadingList.append(presReading)
        outfile.write(str(sensorID)+","+str(city)+","+str(presReading))
        response=input("Enter to continue, 'Q' to stop\n")
    outfile.close()

#ask for sensors' pressure data from user to Data Sensor 2 and keep in dataSensor2.txt
def dataSensor2():
    print("\n-----Data Sensor 2-----\n")
    file2="dataSensor2.txt"
    outfile=open(file2,"w")
    outfile.write("SensorID,City,PressureReading")
    response=''
    while response.upper()!="Q":
        outfile.write("\n")
        sensorID=int(input("Sensor ID: "))
        city=str(input("City: "))
        presReading=eval(input("Pressure Reading: "))
        presReadingList.append(presReading)
        outfile.write(str(sensorID)+","+str(city)+","+str(presReading))
        response=input("Enter to continue, 'Q' to stop\n")
    outfile.close()

#to display and combine the data from both textfiles
def retrieveSensorsRecord():
    print("="*40)
    print("----Data Sensor 1 Pandas DataFrame----\n")
    df1 = pd.read_csv("dataSensor1.txt", sep=",")
    print(df1.to_string())
    print("="*40)
    print("----Data Sensor 2 Pandas DataFrame----\n")
    df2 = pd.read_csv("dataSensor2.txt", sep=",")
    print(df2.to_string())
    concatDataSensorsAndOthers(df1,df2)  #function call

#function to combine textfiles, display highest, lowest and average
def concatDataSensorsAndOthers(df1,df2):
    print("="*40)
    print("-----Concatenated Pandas DataFrame-----\n")
    df3=pd.concat([df1,df2],ignore_index=True,axis=0)
    print(df3)
    highest(df3)  #function call
    lowest(df3)   #function call
    average(df3)  #function call

#function to select highest reading
def highest(df4):
    print("="*40)
    print("Highest Reading Details:\n")
    a=df4[df4["PressureReading"]==df4.PressureReading.max()]
    print(a.max())
    #select_highest=df4.max()


#function to select lowest reading
def lowest(df5):
    print("="*30)
    print("Lowest Reading Details:\n")
    b = df5[df5["PressureReading"] == df5.PressureReading.min()]
    print(b.min())

#function to calculate average pressure reading
def average(df6):
    print("="*40)
    average=(sum(presReadingList))/len(presReadingList)
    print("Average pressure reading: %.3f psi"%average)

#main program
dataSensor1()
dataSensor2()
retrieveSensorsRecord()


