import win10toast as w

toast=w.ToastNotifier()
url="https://w7.pngwing.com/pngs/703/225/png-transparent-man-drinking-water-illustration-fizzy-drinks-carbonated-water-drinking-water-computer-icons-drink-food-hand-logo.png"

toast.show_toast("Reminder","Please drink water in every 10 minutes.",icon_path=url)