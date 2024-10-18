from flask import Flask, request, render_template

app = Flask(__name__)

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            result += chr((ord(char) + shift - shift_amount) % 26 + shift_amount)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        message = request.form["message"]
        shift = int(request.form["shift"])
        action = request.form["action"]
        if action == "Encrypt":
            result = encrypt(message, shift)
        else:
            result = decrypt(message, shift)
        return render_template("index.html", result=result)
    return render_template("index.html", result="")

if __name__ == "__main__":
    app.run(debug=True)
