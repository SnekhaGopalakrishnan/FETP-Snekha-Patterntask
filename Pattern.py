from flask import Flask, render_template, request

app = Flask(__name__)

# Assume successful authentication
authenticated = True

def generate_diamond(num_lines):
    text = "FORMULAQSOLUTIONS"
    text_length = len(text)
    diamond = ""

    # Upper half of the diamond
    for i in range(num_lines // 2 + 1):
        line = "".join([text[j % text_length] for j in range(i * 2 + 1)])
        diamond += line.center(num_lines * 2 - 1) + "\n"

    # Lower half of the diamond
    for i in range(num_lines // 2 - 1, -1, -1):
        line = "".join([text[j % text_length] for j in range(i * 2 + 1)])
        diamond += line.center(num_lines * 2 - 1) + "\n"

    return diamond

@app.route('/')
def home():
    if authenticated:
        return render_template('index.html')
    else:
        return "Authentication failed."

@app.route('/display', methods=['POST'])
def display():
    if authenticated:
        num_lines = int(request.form['num_lines'])
        diamond = generate_diamond(num_lines)
        return "<pre>" + diamond + "</pre>"
    else:
        return "Authentication failed."

if __name__ == '__main__':
    app.run(debug=True)
