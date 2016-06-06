#! /usr/bin/env python
#this code changes de one before
# to make the file executable chmod a+x dnacalc2.py


DNAseq=raw_input ('Enter DNA sequence: ')
DNAseq=DNAseq.upper()
DNAseq=DNAseq.replace(" ", "")

# .uppr doesn't convert the file into uppercase, but instead creates a new string, in uppercase, 
#that will overright the other file.

print ('Sequence is :'+ DNAseq)



SeqLenght= float (len(DNAseq))
print ('Lenght is: ' + str(SeqLenght))

# you cannot have string PLUS number, either convert the 
#number to a string with 'str' or substitute PLUS with COMMA 
#but this might vary between versions of python


NumberA=DNAseq.count('A')
NumberC=DNAseq.count('C')
NumberG=DNAseq.count('G')
NumberT=DNAseq.count('T')
#print ('A: ' + str(NumberA/SeqLenght))
#print ('C: ' + str(NumberC/SeqLenght))
#print ('G: ' + str(NumberG/SeqLenght))
#print ('T: ' + str(NumberT/SeqLenght))
#be careful if they are float or not. The best is to
#change seq lenght to be a float

print ('A: {:.2f}'.format(NumberA/SeqLenght))
# {} for the format function. the ':.f' will say to use 2 
#decimal numbers (f stands for float)
print ('C: {:.2f}'.format(NumberC/SeqLenght))
print ('G: {:.2f}'.format(NumberG/SeqLenght))
print ('T: {:.2f}'.format(NumberT/SeqLenght))

TotalStrong=NumberG+NumberC
TotalWeak=NumberT+NumberA

if SeqLenght<=14:
	MeltTemp=(4*TotalStrong)+(2*TotalWeak)
	
else:
	MeltTemp= 64.9+41*(TotalStrong-16.4)/SeqLenght


print ('Melting Temperature is: {}'.format(MeltTemp))
print('Done')


