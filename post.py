#app.py

from flask import Flask, request #import main Flask class and request object
import base64, os.path, random

app = Flask(__name__) #create the Flask app

@app.route('/converter', methods=['POST']) #GET requests will be blocked

def encode_decode():
    data = request.get_json()

    action_type = data['Type']
    infile = data['InFile']  # absolute file path
    inbase64= data['InBase64']
    outtype = data['OutType']
    outext = data['OutExt']
    outfile = data['OutFile']
    if str(action_type) == "file" and str(outtype) == "base64":
        try:
            data = open(infile, 'rb').read()  # read the file on the server
            encoded = base64.encodestring(data)
            return encoded
        except IOError:
            return 'file not found' + '- ' + infile
    elif str(action_type) == "base64" and str(outtype == "file"):
        try:
            decoded_file = base64.decodestring(inbase64)
            filename = outfile+"."+outext
            if os.path.exists(filename):
                salt = random.randrange(0,1000)
                filename = outfile+"_"+str(salt)+"."+outext
            file_result = open(filename, 'wb')  # create a writable file and write the decoding result
            file_result.write(decoded_file)
            return 'file saved with: '+"- "+filename
        except IOError:
            return 'Can not write file'
    else:
        return action_type


if __name__ == '__main__':
    app.run(debug=True, port=5000) #run app in debug mode on port 5000