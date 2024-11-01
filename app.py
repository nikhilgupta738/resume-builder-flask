from flask import Flask, render_template, request, make_response
import pdfkit

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        data = {
            'fname': request.form['fname'],
            'lname': request.form['lname'],
            'email': request.form['email'],
            'phone': request.form['phone'],
            'website': request.form['web'],
            'linkedin': request.form['linkedin']
        }

        return render_template('preview.html', data=data)
    return render_template('index.html')

@app.route('/preview', methods=['POST'])
def preview():
    data = request.form
    return render_template('preview.html', data=data)
    
@app.route('/download', methods=['POST'])
def download_pdf():
    data = request.form
    rendered = render_template('preview.html', data=data)
    pdf = pdfkit.from_string(rendered, False)
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=resume.pdf'
    return response

if __name__ == '__main__':
    app.run(debug=True)