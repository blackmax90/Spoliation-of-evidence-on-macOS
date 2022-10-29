import Modules.Basic.basic_functions as bf
import Modules.ExtractionConnector as ec
import Modules.AnalyzerConnector as ac
import Modules.TEFT_Display as tdi
from Modules.TEFT_Define import *

import os
import getpass
import shutil
import csv

class TEFT_Core():

    def __init__(self):
        self.traceEviList = ['spotlight', 'msoffice', 'googledrive', 'diagonositc', 'recentfiles', 'documentrevision',
                              'printer', 'web', 'dsstore', 'fseventsd', 'knowledgec', 'notes', 'icloud', 'teams',
                              'slack', 'ichat', 'safari', 'mail', 'gmail']
        self.traceFileList = []
        self.dataForOutput = []
        self.username = ''

    def run(self):

        tdi.run_tool()
        inputType = tdi.select_input()  # 1: Live #2: Dead (Image) #3: Directory

        # Live forensics
        if inputType == '1':

            self.traceFileList = []
            self.dataForOutput = []
            ex_filelist = []
            allfilelist = []

            self.username = getpass.getuser()

            # Create temp folders
            destinationFolder = 'extractedFiles' + ' - ' + self.username
            for traceEvi in self.traceEviList:
                bf.tempFolderCreation(destinationFolder + '/' + traceEvi)

            # Extract trace evidence files
            self.traceEvidenceExtraction('', destinationFolder, self.username)

            # Extract trace file information
            ex_filelist = self.traceEvidenceParser(destinationFolder)

            # Extract all files (except Library folder)
            allfilelist = self.fileExtraction('', self.username)

            # Compare the files
            self.dataForOutput = self.fileComparison(set(ex_filelist), set(allfilelist))

            # Print Output
            self.printOutput(self.username, self.dataForOutput)

        # Input Directory
        elif inputType == '3':

            # Get input folder
            sourceFolder = tdi.type_source_path()
            # Get username
            accountTyped = tdi.type_user_name(sourceFolder)

            # Unknown user account or All user account
            if accountTyped == 'x':

                # Search all user account
                accountList = bf.checkFileInFolder(sourceFolder + '/Users')
                for account in accountList:
                    if account[0] != '.' and account[0] != '_' and account != 'Shared':
                        try:
                            self.username = account

                            # Initialization
                            self.traceFileList = []
                            self.dataForOutput = []
                            ex_filelist = []
                            allfilelist = []

                            # Create temp folders
                            destinationFolder = 'extractedFiles' + ' - ' + self.username
                            for traceEvi in self.traceEviList:
                                bf.tempFolderCreation(destinationFolder + '/' + traceEvi)

                            # Extract trace evidence files
                            self.traceEvidenceExtraction(sourceFolder, destinationFolder, self.username)

                            # Extract trace file information
                            ex_filelist = self.traceEvidenceParser(destinationFolder)

                            # Extract all files (except Library folder)
                            allfilelist = self.fileExtraction(sourceFolder, self.username)

                            # Compare the files
                            self.dataForOutput = self.fileComparison(set(ex_filelist), set(allfilelist))

                            # Print Output
                            self.printOutput(self.username, self.dataForOutput)

                        except:
                            continue

            # User account selected
            else:

                self.traceFileList = []
                self.dataForOutput = []
                ex_filelist = []
                allfilelist = []

                self.username = accountTyped

                # Create temp folders
                destinationFolder = 'extractedFiles' + ' - ' + self.username
                for traceEvi in self.traceEviList:
                    bf.tempFolderCreation(destinationFolder + '/' + traceEvi)

                # Extract trace evidence files
                self.traceEvidenceExtraction(sourceFolder, destinationFolder, self.username)

                # Extract trace file information
                ex_filelist = self.traceEvidenceParser(destinationFolder)

                # Extract all files (except Library folder)
                allfilelist = self.fileExtraction(sourceFolder, self.username)

                # Compare the files
                self.dataForOutput = self.fileComparison(set(ex_filelist), set(allfilelist))

                # Print Output
                self.printOutput(self.username, self.dataForOutput)

        else:
            print("> Error")

    def traceEvidenceExtraction(self, sourceFolder, destinationFolder, username):
        ec.spotlightExtractor(sourceFolder, destinationFolder, username)
        ec.msofficeExtractor(sourceFolder, destinationFolder, username)
        ec.googledriveExtractor(sourceFolder, destinationFolder, username)
        ec.diagnosticExtractor(sourceFolder, destinationFolder, username)
        ec.recentfileExtractor(sourceFolder, destinationFolder, username)
        ec.documentrevisionExtractor(sourceFolder, destinationFolder, username)
        ec.printerExtractor(sourceFolder, destinationFolder, username)
        ec.webExtractor(sourceFolder, destinationFolder, username)
        ec.dsstoreExtractor(sourceFolder, destinationFolder, username)
        ec.fseventsdExtractor(sourceFolder, destinationFolder, username)
        ec.knowledgeCExtractor(sourceFolder, destinationFolder, username)
        ec.notesExtractor(sourceFolder, destinationFolder, username)
        ec.icloudExtractor(sourceFolder, destinationFolder, username)
        ec.teamsExtractor(sourceFolder, destinationFolder, username)
        ec.slackExtractor(sourceFolder, destinationFolder, username)
        ec.ichatExtractor(sourceFolder, destinationFolder, username)
        ec.safariExtractor(sourceFolder, destinationFolder, username)
        ec.mailExtractor(sourceFolder, destinationFolder, username)
        ec.gmailExtractor(sourceFolder, destinationFolder, username)

        print(colored("\n> Extraction Completed", 'yellow'))

    def traceEvidenceParser(self, path_dir):
        temp_list = [] # Initialize
        final_list = []
        try:
            temp_list.append(ac.msofficeParser(path_dir+'/msoffice'))
        except:
            print("ERROR - PARSER - MSOFFICE")
        try:
            temp_list.append(ac.googledriveParser(path_dir+'/googledrive'))
        except:
            print("ERROR - PARSER - GoogleDrive")
        try:
            temp_list.append(ac.spotlightParser(path_dir+'/spotlight'))
        except:
            print("ERROR - PARSER - Spotlight")
        try:
            temp_list.append(ac.knowledgeCParser(path_dir+'/knowledgec'))
        except:
            print("ERROR - PARSER - knowledgec")
        try:
            temp_list.append(ac.iCloudParser(path_dir+'/icloud'))
        except:
            print("ERROR - PARSER - icloud")
        try:
            temp_list.append(ac.teamsParser(path_dir+'/teams'))
        except:
            print("ERROR - PARSER - Teams")
        try:
            temp_list.append(ac.mailParser(path_dir+'/mail'))
        except:
            print("ERROR - PARSER - mail")
        try:
            temp_list.append(ac.recentfilesParser(path_dir+'/recentfiles'))
        except:
            print("ERROR - PARSER - recentfiles")

        for i in temp_list:
            for j in i:
                final_list.append(j)

        print(colored("\n> Trace Evidence Analysis Completed", 'yellow'))
        return(final_list)

    def fileExtraction(self, sourceFolder, username):
        fullpath = sourceFolder+'/Users/' + username
        allfilelist = []
        for (path, dirs, files) in os.walk(fullpath):
            dirs[:] = [dir for dir in dirs if dir != 'Library']
            for file in files:
                if '.docx' in file or '.xlsx' in file or 'pptx' in file:
                    allfilelist.append(file)

        print(colored("\n> File Listing Completed", 'yellow'))
        return allfilelist

    def fileComparison(self, traceFileList, allfileList):
        resultFileList = []
        for tracefile in traceFileList:
            count = 0
            for existfile in allfileList:
                if tracefile.name == existfile.split('.')[0]:
                #if tracefile.name+'.'+tracefile.ext == existfile:
                    count = 1
                    break
            if count == 0:
                resultFileList.append(tracefile)

        print(colored("\n> File Comparison Completed", 'yellow'))
        return resultFileList

    def printOutput(self, username, dataForOutput):
        des = 'Result/'+username
        bf.tempFolderCreation(des)
        f = open(des+'/result.csv', 'w', newline='')
        wr = csv.writer(f)
        wr.writerow(
            ['Filename', 'Extention', 'Filepath', 'Accessed Timestamp', 'Modified Timestamp', 'Filesize', 'Type',
             'Source'])
        for i in range(0, len(dataForOutput)):
            wr.writerow(
                [dataForOutput[i].name, dataForOutput[i].ext, dataForOutput[i].path,
                 dataForOutput[i].a_timestamp, dataForOutput[i].m_timestamp, dataForOutput[i].size,
                 dataForOutput[i].type, dataForOutput[i].source])

        f.close()

if __name__ == '__main__':

    mj = TEFT_Core()
    mj.run()

    print(colored("\n\n--- Completed", 'blue'))

