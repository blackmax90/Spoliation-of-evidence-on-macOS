import Modules.Basic.basic_functions as bf
import Modules.ExtractionConnector as ec
import Modules.AnalyzerConnector as ac

import os
import getpass
import shutil
import csv

global username

traceEviList = ['spotlight', 'msoffice', 'googledrive', 'diagonositc', 'recentfiles', 'documentrevision', 'printer',
                'web', 'dsstore', 'fseventsd', 'knowledgec', 'notes', 'icloud', 'teams', 'slack', 'ichat', 'safari',
                'mail', 'gmail'
                ]

#1

def traceEvidenceExtraction(sourceFolder, username):
    ec.spotlightExtractor(sourceFolder, username)
    ec.msofficeExtractor(sourceFolder, username)
    ec.googledriveExtractor(sourceFolder, username)
    ec.diagnosticExtractor(sourceFolder, username)
    ec.recentfileExtractor(sourceFolder, username)
    ec.documentrevisionExtractor(sourceFolder, username)
    ec.printerExtractor(sourceFolder, username)
    ec.webExtractor(sourceFolder, username)
    ec.dsstoreExtractor(sourceFolder, username)
    ec.fseventsdExtractor(sourceFolder, username)
    ec.knowledgeCExtractor(sourceFolder, username)
    ec.notesExtractor(sourceFolder, username)
    ec.icloudExtractor(sourceFolder, username)
    ec.teamsExtractor(sourceFolder, username)
    ec.slackExtractor(sourceFolder, username)
    ec.ichatExtractor(sourceFolder, username)
    ec.safariExtractor(sourceFolder, username)
    ec.mailExtractor(sourceFolder, username)
    ec.gmailExtractor(sourceFolder, username)

def traceEvidenceParser(path_dir):
    ac.msofficeParser(path_dir+'/msoffice')
    ac.googledriveParser(path_dir+'/googledrive')
    ac.spotlightParser(path_dir+'/spotlight')
    ac.knowledgeCParser(path_dir+'/knowledgec')
    ac.iCloudParser(path_dir+'/icloud')
    ac.teamsParser(path_dir+'/teams')
    ac.mailParser(path_dir+'/mail')
    ac.recentfilesParser(path_dir+'/recentfiles')

    return(ac.finalDataList())

def fileExtraction(sourceFolder, username):
    fullpath = sourceFolder+'/Users/' + username
    allfilelist = []
    for (path, dir, files) in os.walk(fullpath):
        for directory in dir:
            if directory != 'Library':
                for file in files:
                    if '.docx' in file or '.xlsx' in file or 'pptx' in file:
                        allfilelist.append(file)

    return allfilelist

def fileComparison(traceFileList, allfileList):
    resultFileList = []
    for tracefile in traceFileList:
        count = 0
        for existfile in allfileList:
            if tracefile.name+'.'+tracefile.ext == existfile:
                count = 1
        if count == 0:
            resultFileList.append(tracefile)
            '''
            print(str(tracefile.name+'.'+tracefile.ext)+ '|' + str(tracefile.path)+'|'+
                  str(tracefile.a_timestamp)+'|'+str(tracefile.m_timestamp)+'|'+
                  str(tracefile.size)+'|'+str(tracefile.type)+'|'+str(tracefile.source)
                  )
            '''
    return resultFileList

if __name__ == '__main__':


    traceFileList = []
    dataForOutput = []
    execMethod = input("Select the analysis method:\n 1. Live System\n 2. Directory\n>>> ")
    if execMethod == '1':
        username = getpass.getuser()
        for traceEvi in traceEviList:
            tempFolderCreation('extractedFiles' + '/' + traceEvi)

        traceEvidenceExtraction('',username)  # Extract trace evidence files
        traceEvidenceParser('extractedFiles')  # Extract trace file information
        allfilelist = fileExtraction('',username)  # Extract all files (except Library folder)
        dataForOutput = fileComparison(set(traceFileList), set(allfilelist))  # Compare the files

        print("> Completed")

    elif execMethod == '2':
        sourceFolder = input("Please type the source folder (Absolute Path):\nex) /Users/account/Desktop/source (macOS)\nex) D:/source (WindowsOS)\n>>> ")
        accountTyped = input("Please type the user name: (if you don't know the user name, type 'x')\n>>> ")

        if accountTyped == 'x':
            accountList = bf.checkFileInFolder(sourceFolder+'/Users')
            for account in accountList:
                if account[0] != '.' and account[0] != '_' and account != 'Shared':
                    try:
                        userAccount = account
                        for traceEvi in traceEviList:
                            bf.tempFolderCreation('extractedFiles' + '/' + traceEvi)
                        traceEvidenceExtraction(sourceFolder, account)
                        traceFileList = traceEvidenceParser('extractedFiles')  # Extract trace file information
                        allfilelist = fileExtraction(sourceFolder, userAccount)  # Extract all files (except Library folder)
                        dataForOutput = fileComparison(set(traceFileList), set(allfilelist))  # Compare the files

                    except:
                        continue
        else:
            userAccount = accountTyped
            for traceEvi in traceEviList:
                bf.tempFolderCreation('extractedFiles' + '/' + traceEvi)
            traceEvidenceExtraction(sourceFolder, userAccount)
            traceEvidenceParser('extractedFiles')  # Extract trace file information
            allfilelist = fileExtraction(sourceFolder, userAccount)  # Extract all files (except Library folder)
            dataForOutput = fileComparison(set(traceFileList), set(allfilelist))  # Compare the files

    else:
        print("Error")

    bf.tempFolderCreation('Result')
    f = open('Result/result.csv', 'w', newline='')
    wr = csv.writer(f)
    wr.writerow(['Filename', 'Extention', 'Filepath', 'Accessed Timestamp', 'Modified Timestamp', 'Filesize', 'Type', 'Source'])
    for i in range(0, len(dataForOutput)):
        wr.writerow([dataForOutput[i].name, dataForOutput[i].ext, dataForOutput[i].path, dataForOutput[i].a_timestamp,
                    dataForOutput[i].m_timestamp, dataForOutput[i].size, dataForOutput[i].type, dataForOutput[i].source])
    f.close()

    print("\n---Completed")
