import matplotlib.pyplot as plt  # מייבא את הספריה לציור גרפים

# נתונים מומצאים (X,Y)
x = [1, 2, 3, 4, 5]  # רשימת ערכים לציר ה-X
y = [2, 3, 5, 6, 7]  # רשימת ערכים מתאימים לציר ה-Y

# plt.plot(x, y)                # מצייר קו בין כל הנקודות (ללא סימונים מיוחדים)
plt.plot(x, y, marker="o")    # מצייר קו נוסף, ומסמן את הנקודות בעיגול
plt.title("Simple Line Plot") # מוסיף כותרת לגרף
plt.xlabel("X values")        # מוסיף תווית (שם) לציר ה-X
plt.ylabel("Y values")
plt.savefig("../outputs/line_plot.png")
plt.show()                    # מציג את הגרף בחלון נפרד