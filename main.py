import PyPDF2

#Create a list with the file paths
pdfiles = ["./1.pdf", "./2.pdf" , "./3.pdf"]

#Create an instance of PdfFileMerger() class
merger = PyPDF2.PdfMerger()

#Iterate over the list of the file paths
for file in pdfiles:
    #Append each pdf file
    merger.append(file)

#Write the merge pdf file
merger.write('merged.pdf')
merger.close()

print("Merging has been successfully done")
