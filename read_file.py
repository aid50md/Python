# Program to read a file line by line into an raary
# call an internal python function to open, read afile
def file_read(fname):
# create an array
        content_array = {}
# open a file to read
        with open(fname) as f:
            for line in f:
                content_array.append(line)
            print(content_array)
file_read('test.txt')


