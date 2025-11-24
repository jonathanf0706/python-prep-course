import numpy as np

# שני מערכים לחישובים
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print(a + b)   # חיבור איבר-לאיבר
print(a * b)   # כפל איבר-לאיבר
print(a * 2)   # כפל בסקלר
print(a ** 2)  # כל איבר בחזקת 2

# פונקציות מתמטיות
arr = np.array([1, 4, 9, 16])
print(np.sqrt(arr))   # שורש
print(np.log(arr))    # לוג טבעי
print(np.exp(arr))    # e^x

# סטטיסטיקה
data = np.array([1,2,3,4,5,6,7,8,9,10])
print(np.mean(data))  # ממוצע
print(np.std(data))   # סטיית תקן
print(np.sum(data))   # סכום
print(np.min(data))   # הכי קטן
print(np.argmax(data)) # מיקום של הגדול ביותר

# מטריצות
m = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

print(np.sum(m, axis=0))  # סכום לפי עמודות
print(np.sum(m, axis=1))  # סכום לפי שורות


arr = np.array([5, 10, 20, 40])

print(np.sqrt(arr))
print(np.mean(arr))
print(arr * 3)

m = np.array([
    [10, 20, 30],
    [5, 15, 25],
    [2, 4, 6]
])

print(np.mean(m, axis=0))  # 1
print(np.mean(m, axis=1))  # 2
print(np.max(m, axis=0))   # 3


scores = np.array([
    [85, 92, 78, 88],
    [90, 85, 95, 87],
    [78, 88, 84, 90],
    [92, 94, 89, 91],
    [88, 86, 90, 85]
])

print(scores.mean(axis=1))
print(scores.mean(axis=0))
print(scores.max())


m = np.array([
    [2, 4, 6],
    [1, 3, 5],
    [7, 9, 11]
])


def normalize_rows(m):
    v = np.sum(m, axis=1)  # סכום לפי שורות
    m = m / v.reshape(3,1)
    print(v)
    return m

print(normalize_rows(m))

print(np.floor(m * 0.3))


def highlight_edges(m: np.ndarray) -> np.ndarray:
    m[0:-1,0:-1] = False
    m[0,:] = True
    m[-1,:] = True
    m[:,0] = True
    m[:,-1] = True
    return m

print(highlight_edges(m))

