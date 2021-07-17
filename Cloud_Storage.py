import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        f= open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A0w-e2NYVm3-YgHE4ZYCStbIpV-Hil9JJsXuUmO2yff-mCStdxH4YT939p0DCO1vUuFt9ud5FeotmantCg8M5NkXhOPdlH5n0FbVK6OtfjQjJ4s85qbbyGrUzhPGk6oSqvd2chA'
    transferData = TransferData(access_token)

    file_from = input("enter the file path to transfer : -")
    file_to = inpout("enter the full path to upload to dropbox : -")

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved")
main()
# enumerate the local files recursively
for root, dirs, files in os.walk(file_form):

    # construct the full dropbox path
    relative_path = os.path.relpath(local_path, file_from)
    dropbox_path = os.path.join(file_to, relative_path)

    # uploading the file
    with open(local_path, 'rb') as f:
        dbx.files_upload(f.read(), dropbox_path, mode= WriteMode('overwrite'))