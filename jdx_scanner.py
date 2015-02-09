'''
Author: Blake Collins

Description:
<summary of this program>
'''
    
def scanner(file):
    '''
    The scanner function opens a jdx file, scans the document line by line, and finds 
	the Delta-X number and First-X. Delta-X is the number that x is incremented by. X starts
	at First-X. 
    '''
    file_scanner = open(file,"r")
    file_name = input("What would you like to name your file? Remember to add a .txt to the end.  ")
    
    

    for line in file_scanner:
        if line[0:8] == "##DELTAX":
            delta_number = line[9:]
        elif line[0:8] == "##FIRSTX":
            x_val = line[9:]
            return (x_val, delta_number,file_name)


def writer(x_val,delta_number,file_name,file):
    '''
	Writer reopens the file and copies line by line any data that pertains to Absorbance. It writes
	a new line with the x value incremented by the Delta-X value. For my own reference, it also
	writes where specific zones lie and what resides in those groups.   
    '''
    new_file = open(file_name,"w")
    counter = float(x_val)
    x_val = float(x_val)
    delta_number = float(delta_number)
    file_scanner = open(file,"r")
    for line in file_scanner:
        if line[0] != "#" and line[0] != "C" and line[0] != "o":
            linely = line.split()
            for numbers in linely:
                if numbers == linely[0]:
                    pass
                else:
                    new_file.write(str(counter) + " = " + str(numbers) + "\n")
                    counter += delta_number
        if counter >= 1450 and counter < 1700:
            new_file.write("*****Zone 5: Alkene double bonds and aromatic carbon–carbon bonds*****\n")
        elif counter >= 1650 and counter < 2000:
            new_file.write("*****Zone 4: Ester, aldehyde, ketone, carboxylic acid, or amide functional groups*****\n")
        elif counter >= 2100and counter < 2300:
            new_file.write("*****Zone 3: Alkyne triple bonds and nitrile triple bonds*****\n")
        elif counter >= 2700and counter < 3200:
            new_file.write("*****Zone 2:  Aldehyde C-H bonds, and carboxylic acid C-H bonds*****\n")
        elif counter >= 3200 and counter < 3700:
            new_file.write("*****Zone 1:  The alcohol O-H, the terminal alkyne C-H, and the amine or amide N-H*****\n")
    new_file.close()





#==========================================================
def main():
    '''
	Where it all happens. 
    '''

    to_open = input("Name of file to open: ")
    x_val, delta_number,file_name = scanner(to_open)
    writer(x_val, delta_number,file_name,to_open)














if __name__ == '__main__':
    main()
