import os
import logging
from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.middleware.proxy_fix import ProxyFix

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create the app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key-change-in-production")
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

@app.route('/')
def index():
    """Main page route"""
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    """Handle contact form submission"""
    try:
        name = request.form.get('name', '').strip()
        phone = request.form.get('phone', '').strip()
        email = request.form.get('email', '').strip()
        service = request.form.get('service', '').strip()
        message = request.form.get('message', '').strip()
        
        # Basic validation
        if not name or not phone or not email:
            flash('Please fill in all required fields.', 'error')
            return redirect(url_for('index') + '#contact')
        
        # Log the form submission (in production, you'd save to database or send email)
        app.logger.info(f"Contact form submission: Name={name}, Phone={phone}, Email={email}, Service={service}")
        
        flash('Thank you for your message! We will contact you soon.', 'success')
        return redirect(url_for('index') + '#contact')
        
    except Exception as e:
        app.logger.error(f"Error processing contact form: {str(e)}")
        flash('There was an error processing your request. Please try again.', 'error')
        return redirect(url_for('index') + '#contact')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
