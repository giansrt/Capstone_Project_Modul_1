# File: coba_ascii.py

def print_ascii_art():
    # ASCII art of a spaceship
    spaceship = [
"            \\ \\      / /__| | ___ ___  _ __ ___   ___  | |_ ___              ",
"             \\ \\ /\\ / / _ \\ |/ __/ _ \\| '_ ` _ \\ / _ \\ | __/ _ \\             ",
"              \\ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |            ",
" ____          \\_/\\_/ \\___|_|\\___\\___/|_| |_| |_|\\___|  \\__\\___/  _        _ ",
"|  _ \\ ___  _   _  __ _| |  / ___|__ _ _ __ ___  |  _ \\ ___ _ __ | |_ __ _| |",
"| |_) / _ \\| | | |/ _` | | | |   / _` | '__/ __| | |_) / _ \\ '_ \\| __/ _` | |",
"|  _ < (_) | |_| | (_| | | | |__| (_| | |  \\__ \\ |  _ <  __/ | | | || (_| | |",
"|_| \\_\\___/ \\__, |\\__,_|_|  \\____\\__,_|_|  |___/ |_| \\_\\___|_| |_|\\__\\__,_|_|",
"            |___/                                                             "
    ]

    # Print each line of the ASCII art spaceship
    for line in spaceship:
        print(line)

    # ASCII art of a car
    car = [
"  ___",
"    _-_-  _/\\______\\__",
" _-_-__  / ,-. -|-  ,-.`-.",
"-_- _-_- `( o )----( o )-'",
"           `-'      `-'"
    ]

    # Print each line of the ASCII art car
    for line in car:
        print(line)

# Panggil fungsi untuk mencetak ASCII art
print_ascii_art()
