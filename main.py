from flask import Flask, render_template, request
import uuid
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    # If the user clicked the BURN button (POST request)
    if request.method == 'POST':
        # Generate a unique cryptographic ID
        cert_id = f"NIA-{str(uuid.uuid4()).split('-')[0].upper()}"
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
        
        # Render the page in 'certificate' mode
        return render_template('index.html', mode='certificate', cert_id=cert_id, timestamp=timestamp)

    # Otherwise, show the input screen (GET request)
    return render_template('index.html', mode='input')

if __name__ == '__main__':
    # Run the app
    app.run(debug=True, port=5000)
