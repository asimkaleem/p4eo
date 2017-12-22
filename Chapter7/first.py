# fh_1 = open('1.log')
# count = 0
# for lines in fh_1:
#     count = count+1
#     print(lines.lstrip())
# print ("Total Lines:", count)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Read the complete file first and then print the details and work upon it

file_name = input("Please enter the file name: ")

try:
    file_handle = open(file_name)
except:
    print("File can not be open:", file_name)
    quit()

def parse_file(to_look_for):
    for line in com_file:
        line = line.rstrip()
        if not to_look_for in line:
            continue
        # cli_warning = cli_warning + 1
        return(line)
#
#
# print("To Look For: ",parse_file(my_search_str))
