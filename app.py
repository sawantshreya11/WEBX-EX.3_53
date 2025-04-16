from flask import Flask, render_template, request

app = Flask(__name__)

# Homepage Route (Handles GET request with query parameter)
@app.route('/')
def home():
    name = request.args.get('name', 'Guest')
    return render_template('index.html', name=name)

# Contact Page Route
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Handle Form Submission (POST Method)
@app.route('/thank_you', methods=['POST'])
def thank_you():
    name = request.form.get('name')
    email = request.form.get('email')
    return render_template('thank_you.html', name=name, email=email)

if __name__ == '__main__':
    app.run(debug=True)
