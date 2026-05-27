from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

responses = {

    "hello": "Hi! Welcome to Cloud AI Chatbot ☁️",
    "hi": "Hello! How can I help you today?",
    "how are you": "I'm doing great! Thanks for asking.",
    "bye": "Goodbye! Have a nice day.",

    "what is cloud computing": "Cloud computing delivers computing services over the internet.",

    "what is aws": "AWS stands for Amazon Web Services. It provides cloud services like storage, servers and databases.",

    "what is azure": "Azure is Microsoft's cloud platform used for hosting and cloud services.",

    "what is devops": "DevOps combines software development and IT operations to improve deployment speed.",

    "what is python": "Python is a popular programming language used in AI, web development and automation.",

    "what is flask": "Flask is a lightweight Python framework used to build web applications.",

    "what is chatbot": "A chatbot is a program that can communicate with users automatically.",

    "what is ai": "Artificial Intelligence enables machines to simulate human intelligence.",

    "what is machine learning": "Machine learning is a branch of AI where systems learn from data.",

    "what is github": "GitHub is a platform used for storing and managing code repositories.",

    "what is linux": "Linux is an open-source operating system widely used in servers and cloud systems.",

    "what is docker": "Docker is a tool used to create and manage containers.",

    "what is kubernetes": "Kubernetes helps manage containerized applications.",

    "who created you": "I was created using Python, Flask, HTML, CSS and JavaScript.",

    "help": "You can ask me about Cloud, AWS, Python, Flask, AI, DevOps, Docker and Linux.",

    "services": "I provide cloud computing and AI chatbot assistance.",

    "contact": "Contact us at support@cloudbot.com"

}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_message = request.args.get('msg').lower()

    response = responses.get(
    user_message,
    "I'm still learning 🤖. Please ask me about Cloud, AWS, Python, DevOps or AI."
)

    return jsonify(response=response)

if __name__ == "__main__":
app.run(host="0.0.0.0", port=5000)