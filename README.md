USSD-AI Support System
A secure USSD-based support system integrated with AI for providing confidential assistance to vulnerable individuals. This system enables access to support services through basic mobile phones without requiring internet connectivity or smartphones.
🔒 Security Notice
This system handles sensitive information. Please ensure proper security measures are implemented before deployment:

Use environment variables for all API keys and sensitive credentials
Implement proper data encryption
Follow local data protection regulations
Regularly audit system access and usage
Implement secure data retention policies

📋 Prerequisites

Python 3.8+
Africa's Talking account
OpenAI API access
SQLite3
Flask

🔧 Installation

Clone the repository:

bashCopygit clone [repository-url]
cd ussd-ai-support

Create and activate virtual environment:

bashCopypython -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install required packages:

bashCopypip install -r requirements.txt

Set up environment variables:

bashCopyexport AT_USERNAME="your_africastalking_username"
export AT_API_KEY="your_africastalking_api_key"
export OPENAI_API_KEY="your_openai_api_key"
🚀 Configuration
Database Setup
The system automatically creates a SQLite database with the following structure:
sqlCopyCREATE TABLE cases (
    phone_number TEXT,
    session_id TEXT,
    case_type TEXT,
    language TEXT,
    timestamp DATETIME
)
Africa's Talking Configuration

Register at Africa's Talking
Create a new application
Configure USSD callback URL
Note down API credentials

OpenAI Configuration

Obtain API key from OpenAI
Configure response parameters in generate_ai_response()

📱 USSD Menu Structure
CopyWelcome to Confidential Support
1. Get help in English
2. Get help in Swahili
3. Emergency contact
4. Find local support

[After language selection]
Select type of support needed:
1. Information
2. Emergency help
3. Connect with counselor
4. Report case
🛠️ Usage
Starting the Server
bashCopypython app.py
Testing Locally

Use ngrok to expose local server:

bashCopyngrok http 5000

Update Africa's Talking callback URL with ngrok URL

🔐 Privacy Considerations

All user data is stored securely
Phone numbers are encrypted before storage
Session data is temporary
No personal identifiers are logged
AI responses are generated with privacy in mind

⚠️ Important Safety Features

Emergency Contact Integration
Quick Exit Options
Local Support Center Connection
Multi-language Support
Anonymous Case Handling

📊 Monitoring and Logging
The system includes:

Session tracking
Case type monitoring
Language preference tracking
Timestamp logging
Response time monitoring

🔄 Maintenance
Regular maintenance tasks:

Database cleanup
Log rotation
Security updates
AI prompt optimization
Emergency contact verification

🤝 Contributing
Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.
📝 License
This project is licensed under the MIT License - see the LICENSE.md file for details.
🆘 Support and Contact
For support:

Technical issues: [contact details]
Emergency support: [emergency contact]
General inquiries: [email]

🔍 Additional Resources

Africa's Talking Documentation
OpenAI API Documentation
Flask Documentation
Security Best Practices

⚖️ Ethical Guidelines

User Privacy Protection
Data Minimization
Informed Consent
Cultural Sensitivity
Accessibility
Emergency Response Protocol
Regular Ethics Review

🌍 Localization
The system supports multiple languages and can be extended to include:

Additional local languages
Cultural considerations
Local emergency services
Regional support resources

📈 Future Enhancements

Additional language support
Enhanced AI response customization
Expanded emergency services integration
Advanced analytics and reporting
Support group integration

Remember to regularly review and update all security measures and emergency contact information.