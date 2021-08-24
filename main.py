from ronacheck import get_ronastats, get_ronacases
from win10toast import ToastNotifier

stats = get_ronastats()

complete_string = f"""
{stats[0]}
{stats[1]}
"""

for stat in stats:
    print(stat)

toast = ToastNotifier()
toast.show_toast("RonaCheck",complete_string,duration=10)