import Modules.Basic.basic_functions as bf
import os

def spotlightExtractor(sourceFolder, destinationFolder, username):
    des = destinationFolder + '/spotlight'
    try:
        fullpath = sourceFolder + '/Users/' + username + '/Library/Application Support/com.apple.spotlight'
        if os.path.isdir(fullpath) == True:
            for file in bf.checkFileInFolder(fullpath):
                if 'com.apple.spotlight.Shortcuts' in file:
                    bf.fileCopy(fullpath + '/' + file, des)
    except:
        print("error - com.apple.spotlight.Shortcuts")

    try:
        fullpath = sourceFolder + '/Users/' + username + '/Library/Metadata/CoreSpotlight/index.spotlightV3'
        if os.path.isdir(fullpath) == True:
            for file in bf.checkFileInFolder(fullpath):
                if 'journalAttr.' in file:
                    bf.fileCopy(fullpath + '/' + file, des)
    except:
        print("error - spotlightV3 (Permission denided)")

    try:
        fullpath = sourceFolder + '/_.Spotlight-V100/Store-V2'
        if os.path.isdir(fullpath) == True:
            for (path, dir, files) in os.walk(fullpath):
                for file in files:
                    if 'journalAttr.' in file:
                        bf.fileCopy(path + '/' + file, des)
    except:
        print("error - Spotlight-V100")

    try:
        fullpath = sourceFolder + '/_.Spotlight-V100/Store-V2'
        if os.path.isdir(fullpath) == True:
            for (path, dir, files) in os.walk(fullpath):
                for file in files:
                    if '_.store.db' in file:
                        bf.fileCopy(path + '/' + file, des)
    except:
        print("error - store.db")

def msofficeExtractor(sourceFolder, destinationFolder, username):
    des = destinationFolder + '/msoffice'
    try:
        fullpath = sourceFolder+'/Users/' + username + '/Library/Containers/com.microsoft.Word/Data/Library/Preferences'
        if os.path.isdir(fullpath) == True:
            for file in bf.checkFileInFolder(fullpath):
                if 'com.microsoft.Word.plist' in file:
                    bf.fileCopy(fullpath + '/' + file, des)
    except:
        print("error - com.microsoft.Word.plist")

    try:
        fullpath = sourceFolder+'/Users/' + username + '/Library/Group Containers/UBF8T346G9.Office/ComRPC32'
        if os.path.isdir(fullpath) == True:
            for file in bf.checkFileInFolder(fullpath):
                if file == 'ComRPCDB':
                    bf.fileCopy(fullpath + '/' + file, des)
                if file == 'ComRPCDB-wal':
                    #bf.fileCopy(fullpath + '/' + file, 'extractedFiles/msoffice/ComRPCDB-wal_bak')
                    bf.fileCopy(fullpath + '/' + file, des)
    except:
        print("error - ComRPCDB")

    try:
        fullpath = sourceFolder+'/Users/' + username + '/Library/Group Containers/UBF8T346G9.Office/MicrosoftRegistrationDB'
        if os.path.isdir(fullpath) == True:
            for file in bf.checkFileInFolder(fullpath):
                if 'MicrosoftRegistrationDB' in file:
                    bf.fileCopy(fullpath + '/' + file, des)
    except:
        print("error - MicrosoftRegistrationDB")

    try:
        fullpath = sourceFolder+'/Users/' + username + '/Library/Containers/com.microsoft.Word/Data/Library/Application Support/Microsoft/Temp'
        if os.path.isdir(fullpath) == True:
            for file in bf.checkFileInFolder(fullpath):
                if 'WRF' in file or 'WRS' in file:
                    bf.fileCopy(fullpath + '/' + file, des)
    except:
        print("error - WRF+WRS")

    try:
        fullpath = sourceFolder+'/Users/' + username + '/Library/Containers/com.microsoft.Word/Data/Library/Preferences'
        if os.path.isdir(fullpath) == True:
            for file in bf.checkFileInFolder(fullpath):
                if 'com.microsoft.Word.securebookmarks.plist' in file:
                    bf.fileCopy(fullpath + '/' + file, des)
    except:
        print("error - com.microsoft.Word.securebookmarks.plist")

def googledriveExtractor(sourceFolder, destinationFolder, username):
    des = destinationFolder + '/googledrive'
    try:
        fullpath = sourceFolder+'/Users/' + username + '/Library/Application Support/Google/DriveFS'
        if os.path.isdir(fullpath) == True:
            for (path, dir, files) in os.walk(fullpath):
                for file in files:
                    if 'metadata_sqlite' in file or 'psid' in file or 'structured_log' in file or 'finder_ext' in file or 'driver_ext' in file:
                            bf.fileCopy(path+'/'+file, des)
    except:
        print("error - Google Drive")

def diagnosticExtractor(sourceFolder, destinationFolder, username):
    des = destinationFolder + '/diagonositc'
    try:
        fullpath = sourceFolder+'/private/var/db/diagnostics/Persist'
        if os.path.isdir(fullpath) == True:
            for file in bf.checkFileInFolder(fullpath):
                if 'tracev3' in file:
                    bf.fileCopy(fullpath + '/' + file, des)
    except:
        print("error - diagnostic-persist-tracev3")

    try:
        fullpath = sourceFolder+'/private/var/db/diagnostics/Special'
        if os.path.isdir(fullpath) == True:
            for file in bf.checkFileInFolder(fullpath):
                if 'tracev3' in file:
                    bf.fileCopy(fullpath + '/' + file, des)
    except:
        print("error - diagnostic-special-tracev3")

    try:
        fullpath = sourceFolder+'/private/var/log/DiagnosticMessages'
        if os.path.isdir(fullpath) == True:
            for file in bf.checkFileInFolder(fullpath):
                if '.asl' in file:
                    bf.fileCopy(fullpath + '/' + file, des)
    except:
        print("error - diagnostic-asl")

def recentfileExtractor(sourceFolder, destinationFolder, username):
    des = destinationFolder + '/recentfiles'
    try:
        fullpath = sourceFolder+'/Users/' + username + '/Library/Application Support/com.apple.sharedfilelist/com.apple.LSSharedFileList.ApplicationRecentDocuments'
        if os.path.isdir(fullpath) == True:
            for file in bf.checkFileInFolder(fullpath):
                if 'com.apple.textedit' in file or 'com.apple.preview' in file:
                    bf.fileCopy(fullpath + '/' + file, des)
    except:
        print("error - com.apple.textedit")

    try:
        fullpath = sourceFolder+'/Users/' + username + '/Library/Application Support/com.apple.sharedfilelist/'
        if os.path.isdir(fullpath) == True:
            for file in bf.checkFileInFolder(fullpath):
                if 'com.apple.LSSharedFileList.RecentDocuments' in file:
                    bf.fileCopy(fullpath + '/' + file, des)
    except:
        print("error - com.apple.LSSharedFileList.RecentDocuments")

def documentrevisionExtractor(sourceFolder, destinationFolder, username):
    des = destinationFolder + '/documentrevision'
    try:
        fullpath = sourceFolder+'/_.DocumentRevisions-V100/db-V1'
        if os.path.isdir(fullpath) == True:
            for file in bf.checkFileInFolder(fullpath):
                if 'db.sqlite' in file:
                    bf.fileCopy(fullpath + '/' + file, des)
    except:
        print("error - documentRevision:db.sqlite (Permission denied)")

    try:
        fullpath = sourceFolder+'/_.DocumentRevisions-V100/_.cs/ChunkStorage/0/0/0'
        if os.path.isdir(fullpath) == True:
            for file in bf.checkFileInFolder(fullpath):
                if file == '1':
                    bf.fileCopy(fullpath + '/' + file, des)
    except:
        print("error - documentRevision:1 (Permission denied)")

def printerExtractor(sourceFolder, destinationFolder, username):
    des = destinationFolder + '/printer'
    try:
        fullpath = sourceFolder+'/private/var/spool/cups'
        if os.path.isdir(fullpath) == True:
            for file in bf.checkFileInFolder(fullpath):
                if 'c0001' in file or 'd0001' in file:
                    bf.fileCopy(fullpath + '/' + file, des)
    except:
        print("error - printer (permission denided)")

def webExtractor(sourceFolder, destinationFolder, username):
    des = destinationFolder + '/web'
    try:
        fullpath = sourceFolder+'/Users/' + username + '/Library/Preferences'
        if os.path.isdir(fullpath) == True:
            for file in bf.checkFileInFolder(fullpath):
                if 'QuarantineEventsV2' in file:
                    bf.fileCopy(fullpath + '/' + file, des)
    except:
        print("error - web:QuarantineEventsV2")

def dsstoreExtractor(sourceFolder, destinationFolder, username):
    des = destinationFolder + '/dsstore'
    try:
        for folder in bf.checkFileInFolder(sourceFolder+'/Users/'+username):
            if folder == '.DS_Store':
                os.mkdir(des+'/root')
                bf.fileCopy(sourceFolder+'/Users/' + username + '/' + folder, des+'/root')
            elif folder[0] == '.' or folder[0] == '_' or folder == 'Library':
                continue
            else:
                for file in bf.checkFileInFolder(sourceFolder+'/Users/'+username+'/'+folder):
                    if 'DS_Store' in file:
                        os.mkdir(des + '/' + folder)
                        bf.fileCopy(sourceFolder+'/Users/'+username+'/'+folder+'/'+file, des + '/' + folder)
    except:
        print("error - dsstore")

def fseventsdExtractor(sourceFolder, destinationFolder, username):
    des = destinationFolder + '/fseventsd'
    try:
        fullpath = sourceFolder+'/_.fseventsd'
        if os.path.isdir(fullpath) == True:
            for file in bf.checkFileInFolder(fullpath):
                bf.fileCopy(fullpath + '/' + file, des)
    except:
        print("error - fseventsd")

def knowledgeCExtractor(sourceFolder, destinationFolder, username):
    des = destinationFolder + '/knowledgec'
    try:
        fullpath = sourceFolder+'/private/var/db/CoreDuet/Knowledge'
        if os.path.isdir(fullpath) == True:
            for file in bf.checkFileInFolder(fullpath):
                if 'knowledgeC' in file:
                    bf.fileCopy(fullpath + '/' + file, des)
    except:
        print("error - knowledgec (Permission denided)")

def notesExtractor(sourceFolder, destinationFolder, username):
    des = destinationFolder + '/notes'
    try:
        fullpath = sourceFolder+'/Users/' + username + '/Library/Group Containers/group.com.apple.notes'
        if os.path.isdir(fullpath) == True:
            for file in bf.checkFileInFolder(fullpath):
                if 'NoteStore.sqlite' in file or 'NoteStore.sqlite-wal' in file:
                    bf.fileCopy(fullpath + '/' + file, des)
    except:
        print("error - notes")

def icloudExtractor(sourceFolder, destinationFolder, username):
    des = destinationFolder + '/icloud'
    try:
        fullpath = sourceFolder+'/Users/' + username + '/Library/Application Support/CloudDocs/session/db'
        if os.path.isdir(fullpath) == True:
            for file in bf.checkFileInFolder(fullpath):
                if 'client' in file or 'server' in file:
                    bf.fileCopy(fullpath + '/' + file, des)
    except:
        print("Event - icloud")

def teamsExtractor(sourceFolder, destinationFolder, username):
    des = destinationFolder + '/teams'
    try:
        fullpath = sourceFolder+'/Users/' + username + '/Library/Application Support/Microsoft/Teams/Cache'
        if os.path.isdir(fullpath) == True:
            for file in bf.checkFileInFolder(fullpath):
                if file[-2:] == '_0':
                    bf.fileCopy(fullpath + '/' + file, des)
    except:
        print("error - teams:random_0")

    try:
        fullpath = sourceFolder+'/Users/' + username + '/Library/Application Support/Microsoft/Teams/IndexedDB/https_teams.live.com_0.indexeddb.leveldb'
        if os.path.isdir(fullpath) == True:
            for file in bf.checkFileInFolder(fullpath):
                if '.log' in file or '.ldb' in file:
                    bf.fileCopy(fullpath + '/' + file, des)
    except:
        print("error - teams:leveldb")

    try:
        fullpath = sourceFolder+'/Users/' + username + '/Library/Application Support/Microsoft/Teams/Local Storage/leveldb'
        if os.path.isdir(fullpath) == True:
            for file in bf.checkFileInFolder(fullpath):
                if '.log' in file or '.ldb' in file:
                    bf.fileCopy(fullpath + '/' + file, des)
    except:
        print("error - teams:localstroage")

def slackExtractor(sourceFolder, destinationFolder, username):
    des = destinationFolder + '/slack'
    try:
        fullpath = sourceFolder+'/Users/' + username + '/Library/Application Support/Slack/Cache/Cache_Data'
        if os.path.isdir(fullpath) == True:
            for file in bf.checkFileInFolder(fullpath):
                if file[-2:] == '_0':
                    bf.fileCopy(fullpath + '/' + file, des)
    except:
        print("error - slack:random_0")

    try:
        fullpath = sourceFolder+'/Users/' + username + '/Library/Application Support/Slack/IndexedDB/https_app.slack.com_0.indexeddb.blob/1/00'
        if os.path.isdir(fullpath) == True:
            for file in bf.checkFileInFolder(fullpath):
                if file == 'a':
                    bf.fileCopy(fullpath + '/' + file, des)
    except:
        print("error - slack:leveldb")

def ichatExtractor(sourceFolder, destinationFolder, username):
    des = destinationFolder + '/ichat'
    try:
        fullpath = sourceFolder+'/Users/' + username + '/Library/Messages'
        if os.path.isdir(fullpath) == True:
            for file in bf.checkFileInFolder(fullpath):
                if 'chat.db' in file:
                    bf.fileCopy(fullpath + '/' + file, des)
    except:
        print("error - chat.db")

    try:
        fullpath = sourceFolder+'/Users/' + username + '/Library/Messages/Archive'
        if os.path.isdir(fullpath) == True:
            for (path, dir, files) in os.walk(fullpath):
                if '.ichat' in files:
                    bf.fileCopy(path + '/' + files, des)
    except:
        print("error - .ichat")

def safariExtractor(sourceFolder, destinationFolder, username):
    des = destinationFolder + '/safari'
    try:
        fullpath = sourceFolder+'/Users/' + username + '/Library/Safari'
        if os.path.isdir(fullpath) == True:
            for file in bf.checkFileInFolder(fullpath):
                if 'Downloads' in file or 'History.db' in file or 'RecentlyClosedTabs' in file:
                    bf.fileCopy(fullpath + '/' + file, des)
    except:
        print("error - safari: default")

    ''' Not working
    try:
    fullpath = sourceFolder+'/Users/' + username + '/Library/Containers/com.apple.Safari/Data/Library/Caches/com.apple.Safari/WebKitCache/Version 16/Records'
    for (path, dir, files) in os.walk(fullpath):
        for file in files:
            if '-blob' in file:
                bf.fileCopy(path.replace('\\','/') + '/' + file, des)
    except:
        print("error - safari: blob")
    '''

    try:
        fullpath = sourceFolder+'/Users/' + username + '/Library/Safari/Favicon Cache'
        if os.path.isdir(fullpath) == True:
            for file in bf.checkFileInFolder(fullpath):
                if 'favicons.db' in file:
                    bf.fileCopy(fullpath + '/' + file, des)
    except:
        print("error - safari: favicons")

def mailExtractor(sourceFolder, destinationFolder, username):
    des = destinationFolder + '/mail'
    '''
    try:
        fullpath = sourceFolder+'/Users/' + username + '/Library/Suggestions/pending'
        if os.path.isdir(fullpath) == True:
            for file in bf.checkFileInFolder(fullpath):
                if file == '1.qdat':
                    bf.fileCopy(fullpath + '/' + file, des)
    except:
        print("error - mail:1qdat")
    '''
    try:
        fullpath = sourceFolder+'/Users/' + username + '/Library/Mail'
        if os.path.isdir(fullpath) == True:
            for (path, dir, files) in os.walk(fullpath):
                for file in files:
                    if 'Envelope Index' in file:
                        bf.fileCopy(path + '/' + file, des)
    except:
        print("error - mail:envelop")

def gmailExtractor(sourceFolder, destinationFolder, username):
    des = destinationFolder + '/gmail'
    try:
        fullpath = sourceFolder+'/Users/' + username + '/Library/Mail'
        if os.path.isdir(fullpath) == True:
            for (path, dir, files) in os.walk(fullpath):
                for file in files:
                    if 'partial.emlx' in file:
                        bf.fileCopy(path + '/' + file, des)
    except:
        print("error - gmail")