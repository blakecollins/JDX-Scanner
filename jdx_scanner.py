'''
Author: Blake Collins

Description:
<summary of this program>
'''
    
def scanner(file):
    '''
    
    '''
    file_scanner = open(file,"r")
    file_name = input("What would you like to name your file? Remember to add a .txt to the end.  ")
    new_file = open(file_name,"w")
    wavenumber = 0

    for line in file_scanner:
        if line[0:8] == "##FIRSTX":
            start_number = line[9:]
            print(start_number)
        if line[0] != "#":
            line.split(" ")
            print(line)
            new_file.write(line)
            
  
    file_scanner.close()
    new_file.close()





#==========================================================
def main():
    '''

    '''

    to_open = input("Name of file to open: ")
    scanner(to_open)















if __name__ == '__main__':
    main()
