#! /usr/bin/env python
#this is a comment

DNAseq ='ATGAAC'
print ('Sequence is :'+ DNAseq)
# this makes the file executable chmod a+x dnacalc.py

SeqLenght= float (len(DNAseq))
print ('Lenght is: ' + str(SeqLenght))

# you cannot have string PLUS number, either convert the 
#number to a string with 'str' or substitute PLUS with COMMA 
#but this might vary between versions of python


NumberA=DNAseq.count('A')
NumberC=DNAseq.count('C')
NumberG=DNAseq.count('G')
NumberT=DNAseq.count('T')
print ('A: ' + str(NumberA/SeqLenght))
print ('C: ' + str(NumberC/SeqLenght))
print ('G: ' + str(NumberG/SeqLenght))
print ('T: ' + str(NumberT/SeqLenght))
 			#be careful if they are float or not. The best is to
 			#change seq lenght to be a float