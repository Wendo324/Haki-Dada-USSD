from flask import Flask, request
import africastalking
import openai
from datetime import datetime
import sqlite3

class USSDAIService:
    def __init__(self):
        # Initialize Africa's Talking
        self.AT_username = "YOUR_USERNAME"
        self.AT_api_key = "YOUR_API_KEY"
        africastalking.initialize(self.AT_username, self.AT_api_key)
        self.ussd = africastalking.USSD
        
        # Initialize AI client
        self.openai_key = "YOUR_OPENAI_KEY"
        openai.api_key = self.openai_key
        
        # Database setup
        self.setup_database()
    
    def setup_database(self):
        conn = sqlite3.connect('support_cases.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS cases
                    (phone_number TEXT, session_id TEXT, 
                     case_type TEXT, language TEXT, 
                     timestamp DATETIME)''')
        conn.commit()
        conn.close()

    def generate_ai_response(self, user_input, language, case_type):
        """Generate appropriate response using AI"""
        prompt = f"""Context: Support service for vulnerable individuals
        User language: {language}
        Case type: {case_type}
        User input: {user_input}
        Generate a helpful, culturally sensitive response."""
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "prompt": prompt}],
            max_tokens=100,
            temperature=0.7
        )
        return response.choices[0].message.content

    def handle_ussd(self, session_id, phone_number, text):
        """Handle USSD sessions and integrate with AI responses"""
        
        # Initial menu
        if text == "":
            return self.render_menu("""
                Welcome to Confidential Support
                1. Get help in English
                2. Get help in Swahili
                3. Emergency contact
                4. Find local support
            """)
        
        # Parse user input
        user_inputs = text.split("*")
        level = len(user_inputs)
        
        if level == 1:
            selection = user_inputs[0]
            if selection == "1":
                self.save_case(phone_number, session_id, "support", "English")
                return self.render_menu("""
                    Select type of support needed:
                    1. Information
                    2. Emergency help
                    3. Connect with counselor
                    4. Report case
                """)
            # Add other language options and services...
        
        # Handle support conversation with AI
        if level >= 2:
            user_message = user_inputs[-1]
            case_info = self.get_case_info(session_id)
            ai_response = self.generate_ai_response(
                user_message, 
                case_info['language'],
                case_info['case_type']
            )
            return self.render_menu(ai_response)
    
    def render_menu(self, message):
        """Format USSD response"""
        return "CON " + message
    
    def save_case(self, phone_number, session_id, case_type, language):
        """Save case information to database"""
        conn = sqlite3.connect('support_cases.db')
        c = conn.cursor()
        c.execute("""INSERT INTO cases VALUES (?, ?, ?, ?, ?)""",
                 (phone_number, session_id, case_type, language, datetime.now()))
        conn.commit()
        conn.close()
    
    def get_case_info(self, session_id):
        """Retrieve case information from database"""
        conn = sqlite3.connect('support_cases.db')
        c = conn.cursor()
        c.execute("""SELECT * FROM cases WHERE session_id = ?""", (session_id,))
        case = c.fetchone()
        conn.close()
        return {
            'phone_number': case[0],
            'case_type': case[2],
            'language': case[3]
        }

# Flask application
app = Flask(__name__)
ussd_service = USSDAIService()

@app.route('/ussd', methods=['POST'])
def ussd_callback():
    session_id = request.values.get("sessionId", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "")
    
    response = ussd_service.handle_ussd(session_id, phone_number, text)
    return response

if __name__ == "__main__":
    app.run(debug=True)
