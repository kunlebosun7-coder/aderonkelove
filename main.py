import tkinter as tk
from tkinter import messagebox
from datetime import date, datetime
import os
import sys
import subprocess

# ============================================================
# ADERONKE ❤️ - 5 DAYS OF LOVE
# ============================================================

HER_NAME = "ADERONKE"
YOUR_NAME = "URIEL"
START_DATE = "2026-09-20"

SONGS = [
    "day1.mp3",
    "day2.mp3",
    "day3.mp3",
    "day4.mp3",
    "day5.mp3"
]

# ============================================================
# FIVE DAYS OF LOVE
# ============================================================

MESSAGES = [
    (
        "Good Morning, ADERONKE ❤️",
        """Good morning, my love. ❤️

Sometimes I think about how randomly we met,
and somehow that random moment became something
I would never want to lose.

You have always been nice to me,
and there is something about you that makes
you impossible to ignore.

You are special.
You are appreciated.
And you are loved.

Have a beautiful day, my crazy woman. 😂❤️

— URIEL ❤️"""
    ),

    (
        "You Actually Found Me 😂❤️",
        """ADERONKE... 😂❤️

You know what still makes me smile?

You saying "Hi" to me on Facebook
because you had actually been looking for me.

Out of all the people on Facebook,
somehow you found URIEL. 😂

And honestly...

I'm glad you did.

Because that little "Hi"
became the beginning of something
very special to me.

— URIEL ❤️"""
    ),

    (
        "My Crazy Woman 😂❤️",
        """Good morning, ADERONKE. ❤️

Let me tell you something...

I love how crazy you are. 😂

You are properly crazy,
and somehow that craziness is one of
the things I love most about you.

Your energy.
Your personality.
The way you do things.

That's YOU.

And I wouldn't want you to become
somebody else.

Stay crazy, my woman. 😂❤️

— URIEL"""
    ),

    (
        "Always On My Neck 😂❤️",
        """ADERONKE 😂❤️

You are ALWAYS on my neck. 😂

Always!

But you know something?

Deep down, I actually like it.

Because behind all that "being on my neck"
is someone who cares,
someone who notices things,
someone who pays attention.

And you've always been nice to me.

So yes...

You can continue being on my neck. 😂❤️

— URIEL ❤️"""
    ),

    (
        "Five Days Wasn't Enough ❤️",
        """ADERONKE ❤️

Five days...

Five different messages.
Five different songs.

But honestly?

Five days could never be enough
to tell you everything I feel.

I still think about how randomly
we met.

You said "Hi" on Facebook
because you had been looking for me.

And somehow, that simple "Hi"
brought you into my life.

You're nice.
You're caring.
You're crazy. 😂
And you're ALWAYS on my neck. 😂❤️

But you're my crazy woman.

And if I had the chance to go back
to that first day...

I'd still answer.

Every single time.

I love you, ADERONKE. ❤️

— URIEL ❤️"""
    )
]

# ============================================================
# GET CURRENT DAY
# ============================================================

def get_day():

    start = datetime.strptime(
        START_DATE,
        "%Y-%m-%d"
    ).date()

    today = date.today()

    difference = (today - start).days

    if difference < 0:
        return 0

    if difference >= 5:
        return 5

    return difference + 1

# ============================================================
# PLAY MUSIC
# ============================================================

def play_music(day):

    filename = SONGS[day - 1]

    folder = os.path.dirname(
        os.path.abspath(__file__)
    )

    filepath = os.path.join(
        folder,
        filename
    )

    if not os.path.exists(filepath):

        messagebox.showerror(
            "Music Not Found",
            filename +
            " was not found.\n\n"
            "Put the MP3 file in the same folder "
            "as main.py."
        )

        return

    try:

        if sys.platform.startswith("win"):

            os.startfile(filepath)

        elif sys.platform == "darwin":

            subprocess.Popen(
                ["open", filepath]
            )

        else:

            subprocess.Popen(
                ["xdg-open", filepath]
            )

    except Exception as error:

        messagebox.showerror(
            "Music Error",
            str(error)
        )

# ============================================================
# FINAL SURPRISE
# ============================================================

def final_reveal():

    reveal_window = tk.Toplevel(root)

    reveal_window.title(
        "One Last Thing ❤️"
    )

    reveal_window.geometry(
        "500x500"
    )

    reveal_window.resizable(
        False,
        False
    )

    reveal_window.configure(
        bg="#ff6f91"
    )

    hearts = tk.Label(
        reveal_window,
        text="❤️  💕  ❤️",
        font=("Arial", 28),
        bg="#ff6f91"
    )

    hearts.pack(
        pady=(30, 10)
    )

    love_title = tk.Label(
        reveal_window,
        text="I LOVE YOU",
        font=("Georgia", 32, "bold"),
        fg="white",
        bg="#ff6f91"
    )

    love_title.pack(
        pady=10
    )

    name_title = tk.Label(
        reveal_window,
        text=HER_NAME,
        font=("Georgia", 27, "bold"),
        fg="white",
        bg="#ff6f91"
    )

    name_title.pack(
        pady=5
    )

    final_message = tk.Label(
        reveal_window,
        text=(
            "You were never just a random person\n"
            "who said 'Hi' on Facebook.\n\n"
            "You became someone very special to me.\n\n"
            "Thank you for being YOU.\n"
            "Thank you for being crazy. 😂\n"
            "And thank you for always being on my neck. 😂❤️\n\n"
            "If I had to choose again...\n"
            "I'd still choose you."
        ),
        font=("Georgia", 12),
        fg="white",
        bg="#ff6f91",
        justify="center"
    )

    final_message.pack(
        pady=15
    )

    close_button = tk.Button(
        reveal_window,
        text="CLOSE ❤️",
        font=("Arial", 10, "bold"),
        fg="#d81b60",
        bg="white",
        relief="flat",
        padx=20,
        pady=7,
        command=reveal_window.destroy
    )

    close_button.pack(
        pady=10
    )

# ============================================================
# UPDATE 5-DAY DISPLAY
# ============================================================

def update_progress(current_day):

    if current_day == 0:

        progress_text.config(
            text="💕 5 DAYS OF LOVE • STARTING TOMORROW 💕"
        )

    else:

        progress_text.config(
            text=f"💕 DAY {current_day} OF 5 💕"
        )

# ============================================================
# TOMORROW MESSAGE
# ============================================================

def update_tomorrow_message(current_day):

    if current_day == 0:

        tomorrow_text.config(
            text="Your first surprise begins tomorrow ❤️"
        )

    elif current_day < 5:

        tomorrow_text.config(
            text="Come back tomorrow for another surprise... ❤️"
        )

    else:

        tomorrow_text.config(
            text="You made it to the final day. ❤️"
        )

# ============================================================
# DISPLAY CURRENT DAY
# ============================================================

def display_day():

    current_day = get_day()

    update_progress(
        current_day
    )

    update_tomorrow_message(
        current_day
    )

    if current_day == 0:

        title_text.config(
            text="Something Special Is Coming ❤️"
        )

        message_text.config(
            text=(
                "ADERONKE ❤️\n\n"
                "This little surprise isn't ready yet.\n\n"
                "Come back on:\n\n"
                "September 15, 2026\n\n"
                "💕💕💕\n\n"
                "— URIEL ❤️"
            )
        )

        music_button.config(
            state="disabled"
        )

        final_button.config(
            state="disabled"
        )

        return

    title, message = MESSAGES[current_day - 1]

    title_text.config(
        text=title
    )

    message_text.config(
        text=message
    )

    music_button.config(
        state="normal",
        text="PLAY MUSIC 🎵",
        command=lambda: play_music(current_day)
    )

    if current_day == 5:

        final_button.config(
            state="normal"
        )

    else:

        final_button.config(
            state="disabled"
        )

# ============================================================
# FLOATING HEARTS
# ============================================================

def create_heart():

    symbols = [
        "❤️",
        "💕",
        "💗",
        "💖"
    ]

    symbol = symbols[
        date.today().day % len(symbols)
    ]

    heart = tk.Label(
        root,
        text=symbol,
        font=("Arial", 14),
        bg="#ff6f91"
    )

    x = (
        date.today().day * 37
    ) % 560

    heart.place(
        x=x,
        y=640
    )

    move_heart(
        heart,
        x,
        640
    )

    root.after(
        1400,
        create_heart
    )

def move_heart(
    heart,
    x,
    y
):

    if y < -30:

        heart.destroy()

        return

    heart.place(
        x=x,
        y=y
    )

    root.after(
        70,
        lambda: move_heart(
            heart,
            x,
            y - 2
        )
    )

# ============================================================
# OPENING ANIMATION
# ============================================================

def opening_animation():

    animation_text.config(
        text="❤️"
    )

    root.after(
        500,
        show_second_animation
    )

def show_second_animation():

    animation_text.config(
        text="❤️❤️"
    )

    root.after(
        500,
        show_third_animation
    )

def show_third_animation():

    animation_text.config(
        text="❤️❤️❤️"
    )

    root.after(
        500,
        finish_animation
    )

def finish_animation():

    animation_frame.destroy()

    create_heart()

# ============================================================
# MAIN WINDOW
# ============================================================

root = tk.Tk()

root.title(
    "For ADERONKE ❤️"
)

root.geometry(
    "600x650"
)

root.minsize(
    500,
    550
)

root.configure(
    bg="#ff6f91"
)

# ============================================================
# OPENING ANIMATION
# ============================================================

animation_frame = tk.Frame(
    root,
    bg="#ff6f91"
)

animation_frame.place(
    relx=0.5,
    rely=0.5,
    anchor="center"
)

animation_text = tk.Label(
    animation_frame,
    text="❤️",
    font=("Arial", 40),
    bg="#ff6f91"
)

animation_text.pack()

animation_message = tk.Label(
    animation_frame,
    text="A little surprise for ADERONKE...",
    font=("Georgia", 14, "italic"),
    fg="white",
    bg="#ff6f91"
)

animation_message.pack(
    pady=10
)

# ============================================================
# TOP HEART
# ============================================================

top_heart = tk.Label(
    root,
    text="❤️",
    font=("Arial", 30),
    bg="#ff6f91"
)

top_heart.pack(
    pady=(5, 0)
)

# ============================================================
# WHITE CARD
# ============================================================

card = tk.Frame(
    root,
    bg="#fffafa"
)

card.pack(
    padx=20,
    pady=5,
    fill="both",
    expand=True
)

# ============================================================
# HEADING
# ============================================================

heading = tk.Label(
    card,
    text="For " + HER_NAME + " ❤️",
    font=("Georgia", 22, "bold"),
    fg="#d81b60",
    bg="#fffafa"
)

heading.pack(
    pady=(8, 1)
)

# ============================================================
# 5 DAYS OF LOVE
# ============================================================

progress_text = tk.Label(
    card,
    text="",
    font=("Arial", 12, "bold"),
    fg="#d81b60",
    bg="#fffafa"
)

progress_text.pack(
    pady=(3, 5)
)

# ============================================================
# TITLE
# ============================================================

title_text = tk.Label(
    card,
    text="",
    font=("Georgia", 16, "bold"),
    fg="#c2185b",
    bg="#fffafa",
    wraplength=480
)

title_text.pack(
    pady=(4, 4)
)

# ============================================================
# MESSAGE
# ============================================================

message_text = tk.Label(
    card,
    text="",
    font=("Georgia", 10),
    fg="#333333",
    bg="#fffafa",
    justify="center",
    wraplength=470
)

message_text.pack(
    padx=15,
    pady=2,
    fill="both",
    expand=True
)

# ============================================================
# TOMORROW MESSAGE
# ============================================================

tomorrow_text = tk.Label(
    card,
    text="",
    font=("Georgia", 9, "italic"),
    fg="#999999",
    bg="#fffafa"
)

tomorrow_text.pack(
    pady=2
)

# ============================================================
# MUSIC BUTTON
# ============================================================

music_button = tk.Button(
    card,
    text="PLAY MUSIC 🎵",
    font=("Arial", 9, "bold"),
    fg="white",
    bg="#d81b60",
    activebackground="#ad1457",
    activeforeground="white",
    relief="flat",
    padx=15,
    pady=5
)

music_button.pack(
    pady=4
)

# ============================================================
# FINAL SURPRISE BUTTON
# ============================================================

final_button = tk.Button(
    card,
    text="OPEN YOUR FINAL SURPRISE 💌",
    font=("Arial", 9, "bold"),
    fg="#d81b60",
    bg="#ffe4ec",
    activebackground="#ffd1df",
    relief="flat",
    padx=12,
    pady=5,
    command=final_reveal,
    state="disabled"
)

final_button.pack(
    pady=3
)

# ============================================================
# SIGNATURE
# ============================================================

signature = tk.Label(
    card,
    text="Made with ❤️ by " + YOUR_NAME,
    font=("Georgia", 9, "italic"),
    fg="#d81b60",
    bg="#fffafa"
)

signature.pack(
    pady=(0, 6)
)

# ============================================================
# START
# ============================================================

display_day()

root.after(
    300,
    opening_animation
)

root.mainloop()