file_read_path_c_2 = 'Test_pratique/courant/testSortieOnduleurAvecCoupure/testCourantReseauSansRien3Shifted.txt'
file_read_write_c_2 = 'Test_pratique/courant/testSortieOnduleurAvecCoupure/testCourantReseauSansRien3Shiftedbis.txt'

def adapt_data(file_read_path,file_write_path,shift_value,mult):
    values = []
    with open(file_read_path, 'r') as read_file:
        # Read the file line by line
        for line in read_file:
            #print(line)
            values.append((float(line)*mult) -shift_value)

    print(f"values = {values}")
    # Write the list of values to a file
    with open(file_write_path, 'w') as write_file:
        # Read the file line by line
        for value in values:
            write_file.write(str(value)+"\n")

def CODEPO_adapt_data(file_read_path,file_write_path):
    values = []
    with open(file_read_path, 'r') as read_file:
        # Read the file line by line
        for line in read_file:
            value_meas = int(line)
            if(20<value_meas<50):

                values.append(value_meas)

    # Write the list of values to a file
    with open(file_write_path, 'w') as write_file:
        # Read the file line by line
        for value in values:
            write_file.write(str(value)+"\n")

adapt_data(file_read_path_c_2,file_read_write_c_2,55-9,5)
#CODEPO_adapt_data(file_read_path_c_2,file_read_write_c_2)
