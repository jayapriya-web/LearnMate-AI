from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/learn", methods=["POST"])
def learn():

    data = request.get_json(silent=True) or {}

    topic = data.get("topic", "").strip()
    language = data.get("language", "English")
    goal = data.get("goal", "Understand")

    if not topic:
        return jsonify({
            "error": "Please enter a topic"
        }), 400

    # Simple explanation
    explanation = (
        f"{topic} is an important concept to learn. "
        f"Start with the basic idea and understand the main concepts. "
        f"Learn one concept at a time and connect it with simple examples. "
        f"Practice what you learn with small questions or problems. "
        f"Regular practice will help you understand {topic} better."
    )

    # Questions
    quiz = [
        {
            "question": f"What is {topic}?",
            "options": [
                f"A basic concept related to {topic}",
                "A programming error",
                "A type of computer",
                "None of these"
            ],
            "answer": f"A basic concept related to {topic}"
        },
        {
            "question": f"Why is {topic} important?",
            "options": [
                "It helps in understanding the subject",
                "It is only used for games",
                "It has no practical use",
                "None of these"
            ],
            "answer": "It helps in understanding the subject"
        },
        {
            "question": f"What is a good way to learn {topic}?",
            "options": [
                "Understand concepts and practice",
                "Skip the basics",
                "Only memorize answers",
                "Avoid examples"
            ],
            "answer": "Understand concepts and practice"
        }
    ]

    # Study path
    study_plan = [
        f"Understand the basic idea of {topic}",
        "Learn the important concepts",
        "Study simple examples",
        "Practice with questions",
        "Take a quick revision"
    ]

    return jsonify({
        "topic": topic,
        "language": language,
        "goal": goal,
        "explanation": explanation,
        "quiz": quiz,
        "study_plan": study_plan
    })


if __name__ == "__main__":
    app.run(debug=True)