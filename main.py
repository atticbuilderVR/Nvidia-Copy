from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template_string("""
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
        .Normalize-Button {
            background-color: #19d400;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .Normalize-Button:hover {
            background-color: #16b300;
        }
        .device-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 40px;
            margin-top: 40px;
        }
        .device-card {
            background: #fff;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            padding: 24px;
            max-width: 350px;
            text-align: center;
            transition: box-shadow 0.2s;
        }
        .device-card:hover {
            box-shadow: 0 4px 16px rgba(25,212,0,0.15);
        }
        .device-img {
            width: 100%;
            max-width: 300px;
            height: auto;
            border-radius: 10px;
            margin-bottom: 16px;
        }
        .device-title {
            font-size: 22px;
            font-weight: bold;
            margin-bottom: 8px;
            color: #222;
        }
        .device-price {
            font-size: 20px;
            color: #19d400;
            margin-bottom: 12px;
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
    <p class="text-center-2-5">Learn more about the 5090 here.</p>
    <div style="display: flex; justify-content: center; align-items: center;">
        <button onclick="location.href='/learn-more'" class="Normalize-Button" style="padding: 10px 20px; font-size: 16px;">Learn More</button>
    </div>
    <div class="seperator-2"></div>
    <p class="text-center-2" style="margin-top: 40px;">Our Devices</p>
    <div class="device-container">
        <div class="device-card">
            <img src="https://cdn.thepcenthusiast.com/wp-content/uploads/2024/05/nvidia-rtx-5090-founders-edition-leaks.jpg" alt="Nvidia 5090" class="device-img">
            <div class="device-title">Nvidia 5090</div>
            <div class="device-price">$1999.99</div>
            <button onclick="location.href='/purchase'" class="Normalize-Button" style="padding: 10px 20px; font-size: 16px;">Purchase Item</button>
        </div>
        <div class="device-card">
            <img src="https://m.media-amazon.com/images/I/71K4CkU04bL._AC_SL1500_.jpg" alt="NvidiaTab 10" class="device-img">
            <div class="device-title">NvidiaTab 10</div>
            <div class="device-price">$1999.99</div>
            <button onclick="location.href='/purchase'" class="Normalize-Button" style="padding: 10px 20px; font-size: 16px;">Purchase Item</button>
        </div>
    </div>
</body>
</html>
""")
@app.route("/purchase")
def purchase_item():
    return render_template_string("""
<style>
    body {
        background-color: #f0f0f0;
        font-family: Arial, sans-serif;
    }
    .error {
        text-align: center;
        color: #333;
        font-size: 24px;
        margin-top: 20px;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 2px;
        transition: color 0.3s ease;
        flex-direction: column;
    }
    .error:hover {
        color: #19d400;
    }
    .Normalize-Button {
        background-color: #19d400;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .Normalize-Button:hover {
        background-color: #16b300;
    }
</style>
""")
# Change pages by clicking the button
@app.route("/learn-more")
def learn_more():
    return render_template_string("""
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
        .Normalize-Button {
            background-color: #19d400;
            color: white;
            border: none;
            height: 70px;
            position: absolute;
            justify-content: center;
            padding: 0 20px;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .Normalize-Button:hover {
            background-color: #16b300;
        }
    </style>
    <meta charset="UTF-8">
    <title>Nvidia | Learn More</title>
</head>
<body>
    <p class="text-center">Nvidia.com</p>
    <div class="seperator-1"></div>
    <p class="text-center-2">Learn More About the 5090</p>
    <p class="text-center-2-5">The Nvidia 5090 is the next generation of graphics cards, offering unprecedented performance for gamers and creators.</p>
    <button onclick="location.href='/'" class="Normalize-Button">Back to Menu</button>
    
</body>
</html>
""")

@app.route("/company")
def company_info():
    return render_template_string("""
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
            margin-top: 19px;
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
        .Normalize-Button {
            background-color: #19d400;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .Normalize-Button:hover {
            background-color: #16b300;
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
    <p class="text-center-2-5">Apply for a job here.</p>
    <iframe src="https://forms.gle/FXkCXroYDSznJWbh7" style="width: 100%; height: 500px; border: none;"></iframe>
</body>
</html>
""")
if __name__ == "__main__":
    app.run(debug=True)
