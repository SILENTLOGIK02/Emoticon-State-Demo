emoticon = "(^,^)"

def main():
    global emoticon
    say("I am happy today")
    emoticon = ":)"
    say("because i by pc")

def say(phrase):
    print(phrase+" " +emoticon)

main()