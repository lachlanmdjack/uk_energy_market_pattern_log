from scipy.optimize import curve_fit
import numpy as np
import datetime as dt

DATA = (
    ("21/08/2025", 9.0), ( "26/08/2025", 10.6), ("09/09/2025", 6.0),
    ("24/09/2025", 5.4), ( "19/10/2025", 5.5), ( "26/10/2025", 3.1),
    ("27/10/2025", 4.0), ( "30/10/2025", 4.0), ( "14/11/2025", 2.1),
    ("12/12/2025", 2.7), ( "01/01/2026", 2.0), ( "03/03/2026", 2.4),
    ("13/03/2026", 3.2), ( "31/03/2026", 8.1), ( "15/04/2026", 7.4),
    ("24/04/2026", 9.9), ("02/06/2026", 9.5), ("21/06/2026", 8.9),
    ("30/06/2026", 10.6), ("15/07/2026", 12.1), ("19/07/2026", 13.0),
    ("27/07/2026", 12.4)
)

def day_number(date_str):
    d = dt.datetime.strptime(date_str, "%d/%m/%Y").date()
    return abs((d - dt.date(d.year, 1, 1)).days)+1

def model(t, A, phi, C):
    return A * np.sin(2*np.pi*t/365.25 + phi) + C

t = np.array([day_number(d) for d, _ in DATA], dtype=float)
y = np.array([v for _, v in DATA],dtype=float)
popt, _ = curve_fit(model, t, y, p0=[(y.max()-y.min())/2, 0, y.mean()])
A, phi, C = popt
print(f" A = {A}, phi = {phi}, C = {C}")