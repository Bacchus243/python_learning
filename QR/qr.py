import qrcode

data = 'https://santanweddings.com'

img = qrcode.make(data)

img.save('/Users/trenton/Library/Mobile Documents/com~apple~CloudDocs/Github 2/learning/python learning/QR/myqrcode.png')
