import matplotlib.pyplot as plt


def clean_file(file_read_path,file_write_path,start_index,end_index):
    i=0
    cleaned_value_list = []

    #Construct the list of values in such a way we only keep the values we want

    with open(file_read_path, 'r') as file:
        # Read the file line by line
        for line in file:
            # Process each line
            # For example, you can print each line
            if (start_index<i<end_index):
                cleaned_value_list.append(f"{i*1.5}  # "+ line)
            i+=1

    # Write the list of values to a file
    with open(file_write_path, 'w') as file:
        # Read the file line by line
        for value in cleaned_value_list:

            file.write(value)
    
    return cleaned_value_list
def display_data(cleaned_value_list, filename="test.png"):

    for i in range(len(cleaned_value_list)):
        cleaned_value_list[i] = cleaned_value_list[i].split("  # ")

    x = []
    y = []

    for i in range(len(cleaned_value_list)):
        x.append(float(cleaned_value_list[i][0]))
        y.append(float(cleaned_value_list[i][1]))

    # Plot the data
    plt.plot(x, y)

    # Add labels and title
    plt.xlabel('Temps (ms)')
    plt.ylabel('Tension (V)')
    plt.title('Tension in function of Time')

    # Save the graph to a file
    plt.savefig(filename)

    # Display the graph
    plt.show()
    

def rewrite_data(file_to_read_path,file_to_write_path):
    value_before_hash = []
    value_after_hash = []

    # Read the data from the file
    with open(file_to_read_path, 'r') as file:
        data = file.readlines()
        print(data)

    # Split the data using the '#' symbol as the delimiter and take the second part
    for line in data:
        value_before_hash.append(line.split('#')[0].strip())
        value_after_hash.append(line.split('#')[1].strip())


    with open(file_to_write_path, 'w') as file:
        for value in value_before_hash:
            file.write(value + '\n')
        
def test_bis():
    #Function Temp
    file_to_read_path = 'Test_pratique/tension/testReseauSortieUps/testTensionReseauSortieUps1.txt'
    file_to_write_path = 'Test_pratique/measureTIming'
    file_to_write_path_temp = 'Test_pratique/measureTImingTemp'

    #rewrite_data(file_to_read_path,file_to_write_path)
    cleaned_value_list = clean_file(file_to_write_path,file_to_write_path_temp,0,20000)
    display_data(cleaned_value_list)


def CODEPO_clean_file(file_read_path,file_write_path,start_index,end_index):
    i=0
    cleaned_value_list = []

    #Construct the list of values in such a way we only keep the values we want

    with open(file_read_path, 'r') as file:
        # Read the file line by line
        for line in file:
            # Process each line
            # For example, you can print each line
            if (start_index<i<end_index):
                cleaned_value_list.append(f"{i*20}  # "+ line)
            i+=1

    # Write the list of values to a file
    with open(file_write_path, 'w') as file:
        # Read the file line by line
        for value in cleaned_value_list:

            file.write(value)
    
    return cleaned_value_list

def CODEPO_files_and_display():
    CODEPO_file_read_path1 = 'CODEPO\CurrentGridAdapted.txt'
    CODEPO_file_read_path2 = 'CODEPO\CurrentGrid.txt'
    CODEPO_file_read_path3 = 'CODEPO\TestCouranAC_Adapted.txt'

    CODEPO_file_read_path = 'capteurAvide.txt'

    cleaned_value_list = clean_file(CODEPO_file_read_path2,file_write_path_temp,0,2000/10)

    display_data(cleaned_value_list)
# Specify the file path

file_read_path_c_1 = 'Test_pratique/courant/testCalibrationSansCoupure/ReseauCoupeShifted.txt'
file_read_path_c_2 = 'Test_pratique/courant/testReseauSortieGrandRegAvecCoupure/testCourantReseauSortieGrandReg1Shifted.txt'
file_read_path_c_3 = 'Test_pratique/courant/testReseauSortieUps/testCourantReseauSortieUps1Shifed.txt'
file_read_path_c_4 = 'Test_pratique/courant/testSortieOnduleurAvecCoupure/testCourantReseauSansRien3Shiftedbis.txt'

file_read_path_t_1 = 'Test_pratique/tension/testCalibration/ReseauSansCoupeShifted.txt'
file_read_path_t_2 = 'Test_pratique/tension/testReseauSortieGrandReg/testTensionReseauSortieGrandReg1.txt'
file_read_path_t_3 = 'Test_pratique/tension/testReseauSortieOnduleur/testTensionReseauSansRien1.txt'
file_read_path_t_4 = 'Test_pratique/tension/testReseauSortieUps/testTensionReseauSortieUps1CorrectedShifted.txt'


file_write_path = 'cleaned_data/testCalibration_ReseauCoupe.txt'
file_write_path_temp = 'cleaned_data/temp.txt'

# Specify the file path
file_path = file_read_path_t_3
type_value = "graph/tension/"
filename = type_value+file_path.split('/')[-1].split('.')[0]+".png"

cleaned_value_list = clean_file(file_path,file_write_path,0,20000/10)

display_data(cleaned_value_list,filename)

