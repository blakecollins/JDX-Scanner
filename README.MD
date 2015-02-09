JDX-Scanner is a small program written in Python that reads JDX files from, say, NIST and then parses
information that I am looking for. 

What am I looking for? Specifically, I'm working on extracting the transmittance information for groups of aromatic
molecules. The idea is to examin Luca Turin's theory of smell based on molecular vibration by creating a 
program that can scan jdx files, mark specific peaks, note what typically is in that area, and then, finally,
create a relationtional database between organoleptics and the peaks of the database.

TO DO:
Write a scraper that will find JDX files on the NIST website.
Write a portion of the program that will parse absorbance peaks.
Begin mapping peaks to commonly agreed upon organoleptic data.
