from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """<html lang="en">
<head>
    <style>
        body {
            background-color: #f0f0f0;
            font-family: Arial, sans-serif;
        }
        .text-center, .text-center-2 {
            text-align: center;
            color: #333;
            font-size: 24px;
            margin-top: 20px;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 2px;
            transition: color 0.3s ease;
        }
        .text-center:hover, .text-center-2:hover {
            color: #19d400;
        }
        .text-center-2-5 {
            font-size: 28px;
            margin-top: 10px;
            text-align: center;
            color: #555;
            font-weight: normal;
            text-transform: none;
            letter-spacing: 1px;
            transition: color 0.3s ease;
        }
        .text-center-2-5:hover {
            color: #19d400;
        }
        @media (max-width: 600px) {
            .text-center {
                font-size: 20px;
            }
        }
        .seperator-1, .seperator-2 {
            width: 100%;
            height: 6px;
            background-color: #19d400;
            margin: 20px 0;
        }
    </style>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nvidia</title>
</head>
<body>
    <p class="text-center">Nvidia.com</p>
    <div class="seperator-1"></div>
    <p class="text-center-2">Explore the 5090</p>
    <p class="text-center-2-5">The Graphics Card That Will Change The Way Gamers Play Games</p>
</body>
</html>"""
@app.route("/company")
def company_info():
    return """
<html lang="en">
<head>
    <style>
            body {
            background-color: #f0f0f0;
            font-family: Arial, sans-serif;
        }
        .text-center, .text-center-2 {
            text-align: center;
            color: #333;
            font-size: 24px;
            margin-top: 20px;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 2px;
            transition: color 0.3s ease;
        }
        .text-center:hover, .text-center-2:hover {
            color: #19d400;
        }
        .text-center-2-5 {
            font-size: 28px;
            margin-top: 10px;
            text-align: center;
            color: #555;
            font-weight: normal;
            text-transform: none;
            letter-spacing: 1px;
            transition: color 0.3s ease;
        }
        .text-center-2-5:hover {
            color: #19d400;
        }
        @media (max-width: 600px) {
            .text-center {
                font-size: 20px;
            }
        }
        .seperator-1, .seperator-2 {
            width: 100%;
            height: 6px;
            background-color: #19d400;
            margin: 20px 0;
        }
    </style>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nvidia | Developers</title>

</head>

<body>
    <p class="text-center">Nvidia.com</p>
    <div class="seperator-1"></div>
    <p class="text-center-2">Nvidia Developers</p>
    <p class="text-center-2-5">Empowering Developers to Create the Future of AI and Graphics</p>
</body>
</html>
"""
if __name__ == "__main__":
    app.run(debug=True)
