from customtkinter import *


seconds_in_absolute_year = 31558149.984384

def count_seconds(after, yy, dd, hh, mm, ss):
    """
    Calculates the number of seconds since the beginning of the year.

    Args:
      after: If True, counts seconds after the birth of Jesus Christ.
      yy: Year.
      dd: Day of the year.
      hh: Hour.
      mm: Minute.
      ss: Second.

    Returns:
      The number of seconds.
    """

    seconds = 0

    dd_const = 365
    if after:
        if yy % 400 == 0 or (yy % 4 == 0 and yy % 100 != 0):
            dd_const = 366
    else:
        if yy % 400 == 1 or (yy % 4 == 1 and yy % 100 != 1):
            dd_const = 366

    if 1 <= yy and 1 <= dd <= dd_const and 0 <= hh <= 23 and 0 <= mm <= 59 and 0 <= ss <= 59:
        if after:
            for year in range(yy - 1, 0, -1):
                "високосный"
                if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
                    seconds += 86400 * 366
                else:
                    seconds += 86400 * 365

        else:
            for year in range(yy, 0, -1):
                "високосный"
                if year % 400 == 1 or (year % 4 == 1 and year % 100 != 1):
                    seconds -= 86400 * 366
                else:
                    seconds -= 86400 * 365

        seconds += ss + 60 * mm + 3600 * hh + 86400 * (dd - 1)

    return seconds


def update(event):
    try:
        years = int(years_entry.get())
        days = int(days_entry.get())
        hours = int(hours_entry.get())
        minutes = int(minutes_entry.get())
        seconds = int(seconds_entry.get())
        if is_combobox.get() == "н.э.":
            seconds = count_seconds(True, years, days, hours, minutes, seconds)
        else:
            seconds = count_seconds(False, years, days, hours, minutes, seconds)

        absolute_years = seconds / seconds_in_absolute_year

        # answer_label.configure(text=seconds / 86400)
        answer_label.configure(text=absolute_years)

    except:
        pass



set_appearance_mode("System")
set_default_color_theme("blue")

app = CTk()
app.geometry("1080x720")
app.title("Chronology")
app.resizable(0, 0)

label = CTkLabel(app, text="From default chronology to absolute", font=("Arial", 18))
label.pack()

years_entry = CTkEntry(app)
years_entry.pack()

days_entry = CTkEntry(app)
days_entry.pack()

hours_entry = CTkEntry(app)
hours_entry.pack()

minutes_entry = CTkEntry(app)
minutes_entry.pack()

seconds_entry = CTkEntry(app)
seconds_entry.pack()

is_combobox = CTkComboBox(app, values=["н.э.", "до н.э."], command=update)
is_combobox.pack()

answer_label = CTkLabel(app, text="")
answer_label.pack()


years_entry.bind("<KeyRelease>", update)
days_entry.bind("<KeyRelease>", update)
hours_entry.bind("<KeyRelease>", update)
minutes_entry.bind("<KeyRelease>", update)
seconds_entry.bind("<KeyRelease>", update)

app.mainloop()
