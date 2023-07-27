import os
from flask import Flask, render_template, request, send_file
from flask_frozen import Freezer
import sys

app = Flask(__name__)
freezer = Freezer(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        article_text = request.form['article']
        # Here, you should implement the logic to convert the article into a presentation.
        # For simplicity, we will just pass the article text as is to the presentation template.
        return render_template('presentation.html', article_text=article_text)
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    if request.method == 'POST':
        presentation_text = request.form['presentation_text']
        # Save the presentation text to a temporary file
        temp_file_path = "temp_presentation.txt"
        with open(temp_file_path, "w") as f:
            f.write(presentation_text)

        # Serve the file for download
        try:
            return send_file(temp_file_path, as_attachment=True, attachment_filename='presentation.txt')
        finally:
            # Clean up the temporary file
            os.remove(temp_file_path)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "freeze":
        freezer.freeze()
    else:
        app.run(host='0.0.0.0', port=8080, debug=True)
