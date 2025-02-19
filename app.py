from flask import Flask

app = Flask(__name__)

@app.route('/')
def thank_you():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Thank You</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
            }
            .header {
                background-color: #242424;
                color: white;
                padding: 12.7px;
                display: flex;
                align-items: center;
            }
            .header img {
                height: 24px;
                margin-right: 10px;
            }
            .header h1 {
                font-size: 1.2em;
                margin: 0;
            }
            .sub-header {
                background-color: #c1e5e5;
                padding: 0.5px;
                margin-top: -2px;
            }
            .container {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 80vh;
                text-align: center;
            }
            .message {
                font-size: 1.5em;
            }
        </style>
    </head>
    <body>
        <div class="header">
            <img src="/static/logo.png" alt="Contoso Inc. Logo">
            <h1>i-ARM</h1>
        </div>
        <div class="sub-header">
            <p>&nbsp;&nbsp;&nbsp;&nbsp;My Disposal Dashboard</p>
        </div>
        <div class="container">
            <div class="message">
                Thank you for buying our product. Contact us so we will deploy functionality for you.
            </div>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
    
