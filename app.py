from flask import Flask, render_template
from datetime import date, datetime

app = Flask(__name__)

# ============================================================
# ADERONKE — 5 DAYS OF LOVE
# ============================================================

START_DATE = "2026-09-20"
TEST_MODE = False

DAYS = [
    {
        "day": 1,
        "title": "GOOD MORNING, ADERONKE ❤️",
        "message": (
            "I still think it's funny how randomly you came into my life. "
            "Somehow, that random meeting became something I genuinely treasure."
        ),
        "song": "day1.mp3"
    },

    {
        "day": 2,
        "title": "YOU ACTUALLY FOUND ME, JUST LIKE BABA SAID 😂❤️",
        "message": (
            "You actually saying the first Hi still makes me feel ELATED. "
            "You looked for me, found me, and decided to send that HEY KUNLE."
        ),
        "song": "day2.mp3"
    },

    {
        "day": 3,
        "title": "MY CRAZY WOMAN 😂❤️",
        "message": (
            "I love how crazy you are OMO Pa AWANEBI. "
            "Not the kind of crazy that makes me run away — "
            "the kind that makes life more interesting."
        ),
        "song": "day3.mp3"
    },

    {
        "day": 4,
        "title": "ALWAYS ON MY NECK 😂❤️",
        "message": (
            "You are ALWAYS on my neck. 😂 "
            "And somehow, I've gotten used to it. "
            "Actually... I think I secretly like it."
        ),
        "song": "day4.mp3"
    },

    {
        "day": 5,
        "title": "FIVE DAYS WASN'T ENOUGH ❤️",
        "message": (
            "Five days was never going to be enough. "
            "Because our story isn't just five days. "
            "It's the random talking, the Hi, the craziness, "
            "the laughter, and everything that is still ahead of us."
        ),
        "song": "day5.mp3"
    }
]

# ============================================================
# FIND CURRENT DAY
# ============================================================

def get_current_day():

    if TEST_MODE:
        return 5

    today = date.today()

    start = datetime.strptime(
        START_DATE,
        "%Y-%m-%d"
    ).date()

    difference = (today - start).days

    if difference < 0:
        return 0

    if difference >= 4:
        return 5

    return difference + 1
# ============================================================
# HOME PAGE
# ============================================================

@app.route("/")
def home():

    current_day = get_current_day()

    return render_template(
        "index.html",
        current_day=current_day,
        start_date=START_DATE
    )

# ============================================================
# DAY PAGE
# ============================================================

@app.route("/day/<int:day_number>")
def day(day_number):

    current_day = get_current_day()

    if day_number < 1 or day_number > 5:
        return "Invalid day.", 404

    if current_day == 0:
        return render_template(
            "locked.html",
            message="The surprise hasn't started yet. ❤️"
        )

    if day_number > current_day:
        return render_template(
            "locked.html",
            requested_day=day_number,
            current_day=current_day
        )

    selected_day = DAYS[day_number - 1]

    return render_template(
        "day.html",
        day=selected_day,
        current_day=current_day
    )

# ============================================================
# FINAL SURPRISE
# ============================================================

@app.route("/final")
def final():

    current_day = get_current_day()

    if current_day < 5:
        return render_template(
            "locked.html",
            message="The final surprise isn't ready yet. ❤️",
            current_day=current_day
        )

    return render_template(
        "final.html"
    )

# ============================================================
# RUN APPLICATION
# ============================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )