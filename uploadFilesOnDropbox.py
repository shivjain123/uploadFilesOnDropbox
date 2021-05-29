import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'ksAyx1HqRZ4AAAAAAAAAAXenJVA7FF-0W9et3dBwy9FIOM5mwgoJsck9jU212snd'
    transferData = TransferData(access_token)

    file_from = 'C:/Users/HP/OneDrive/Documents/Python (WhiteHatJr)/.py/test1.txt'
    file_to = '/test_dropbox/test1.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()
