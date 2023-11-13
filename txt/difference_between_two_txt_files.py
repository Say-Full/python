f1 = open("final.txt", "r")
f2 = open("modif.txt", "r")
 
f1_data = f1.readlines()
f2_data = f2.readlines()

line = 0

for f1_line in f1_data :
    for f2_line in f2_data[line:] :
        if f1_line == f2_line:
            print("Baris ke-", line, ": sama")
        else:
            print("Baris ke-", line, " BERBEDA:")
            print("\tFile 1:", f1_line, end='')
            print("\tFile 2:", f2_line, end='')
        break
    
    line += 1

f1.close()
f2.close()