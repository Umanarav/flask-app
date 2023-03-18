from flask import Flask, render_template_string
import random

app = Flask(__name__)

@app.route('/')
def home():
    # Initialize the first two Fibonacci numbers
    fibonacci_nums = [1, 1]

    # Generate the remaining Fibonacci numbers up to 377
    while fibonacci_nums[-1] < 377:
        next_num = fibonacci_nums[-1] + fibonacci_nums[-2]
        fibonacci_nums.append(next_num)

    # Select four random Fibonacci numbers between 13 and 377
    lAmount = random.choice([num for num in fibonacci_nums if num >= 13 and num <= 377])
    sAmount = random.choice([num for num in fibonacci_nums if num >= 13 and num <= 377])
    mAmount = random.choice([num for num in fibonacci_nums if num >= 13 and num <= 377])
    sDegree = random.choice([num for num in fibonacci_nums if num >= 13 and num <= 377])

    template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Turtle Mandala</title>
    </head>
    <body>
        <h1>Turtle Mandala</h1>
        <canvas id="mycanvas" width="677" height="677"></canvas>
        <button onclick="refreshMandala()">Refresh Mandala</button>
        <script type="text/javascript">
            function refreshMandala() {
                location.reload();
            }
            var lAmount = {{ lAmount }};
            var sAmount = {{ sAmount }};
            var mAmount = {{ mAmount }};
            var sDegree = {{ sDegree }};
            var mycanvas = document.getElementById("mycanvas");
            var ctx = mycanvas.getContext("2d");
            ctx.fillStyle = "black";
            ctx.fillRect(0, 0, mycanvas.width, mycanvas.height);
            ctx.strokeStyle = "white";
            var xPos = 233;
            var yPos = 233;
            var angle = 0;
            for (var i = 0; i < lAmount; i++) {
                for (var j = 0; j < sAmount; j++) {
                    ctx.beginPath();
                    ctx.moveTo(xPos, yPos);
                    xPos += Math.cos(angle) * mAmount;
                    yPos += Math.sin(angle) * mAmount;
                    ctx.lineTo(xPos, yPos);
                    angle += sDegree * Math.PI / 180;
                    ctx.stroke();
                }
                angle += 137.5 * Math.PI / 180;
            }
        </script>
    </body>
    </html>
    '''
    return render_template_string(template, lAmount=lAmount, sAmount=sAmount, mAmount=mAmount, sDegree=sDegree)

if __name__ == '__main__':
    app.run()