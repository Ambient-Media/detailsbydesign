# Details by Design - Auto Detailing Website

A premium single-page website for Details by Design auto detailing business in Missoula, Montana. Built with a dark theme, gold accents, and comprehensive service showcase.

## 🚀 AWS Amplify Deployment

This website is optimized for AWS Amplify deployment as a static site.

### Quick Deploy to Amplify

1. **Connect Your Repository**
   - Go to [AWS Amplify Console](https://console.aws.amazon.com/amplify/)
   - Click "Get Started" under "Deploy"
   - Connect your GitHub/GitLab/Bitbucket repository
   - Select this repository and branch

2. **Build Settings**
   - Amplify will automatically detect the `amplify.yml` file
   - No additional build configuration needed
   - The site deploys as a static website

3. **Environment Variables (Optional)**
   - No environment variables required for basic deployment
   - For form functionality, configure Formspree integration (see below)

### Form Handling Setup

The website includes contact forms that need external service integration:

#### Option 1: Formspree Integration
1. Sign up at [Formspree.io](https://formspree.io)
2. Create a new form and get your form ID
3. Replace `YOUR_FORM_ID` in `index.html` with your actual form ID:
   ```html
   <form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
   ```

#### Option 2: AWS SES Integration
1. Set up AWS SES in your AWS account
2. Create a Lambda function to handle form submissions
3. Update form actions to point to your API Gateway endpoint

### Custom Domain (Optional)
1. In Amplify Console, go to "Domain management"
2. Add your custom domain
3. Follow AWS instructions for DNS configuration

## 📁 Project Structure

```
├── index.html          # Main HTML file (static version)
├── amplify.yml         # Amplify build configuration
├── static/
│   ├── style.css       # Main stylesheet
│   ├── script.js       # JavaScript functionality
│   ├── hero-car.jpg    # Hero section image
│   ├── car-detail-close.jpg  # About section image
│   └── wheel-cleaning.jpg    # Reviews section image
├── templates/          # Flask templates (for development)
├── app.py             # Flask application (for development)
└── README.md          # This file
```

## 🎨 Features

- **Responsive Design**: Mobile-first approach with Bootstrap 5
- **Dark Theme**: Professional automotive aesthetic with gold accents
- **Interactive Modal**: Quote request form with validation
- **Customer Reviews**: Authentic Google reviews displayed
- **SEO Optimized**: Local business schema markup included
- **Performance**: Optimized images and minimal dependencies

## 🛠️ Local Development

For local development with Flask:

```bash
# Install dependencies
pip install flask

# Run development server
python app.py
```

For static file testing:
```bash
# Serve static files (Python 3)
python -m http.server 8000

# Or with Node.js
npx serve .
```

## 📱 Mobile Optimization

- Hamburger navigation for mobile devices
- Responsive grid layouts
- Touch-friendly buttons and forms
- Optimized images for different screen sizes

## 🔧 Customization

### Contact Information
Update contact details in `index.html`:
- Phone: `(406) 240-2675`
- Email: `Detailsbydesign18@gmail.com`
- Location: `Missoula, MT`

### Services
Modify the services section to add/remove offerings

### Colors
Primary brand colors defined in CSS:
- Gold: `#ffd700`
- Dark Background: `#000000`
- Secondary Dark: `#111111`

## 📊 Analytics (Optional)

Add Google Analytics by inserting tracking code before closing `</head>` tag:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

## 🔒 Security

- All external links use HTTPS
- Form validation on client-side
- No sensitive data stored in repository
- CDN resources from trusted providers

## 📞 Support

For technical support or customization requests, contact the development team.

## 📄 License

This project is proprietary to Details by Design. All rights reserved.