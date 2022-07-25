def delay_print(text, delay):
    for i in text:
        time.sleep(delay)
        print(i, end='')
        sys.stdout.flush()
    print()

delay_print("Ylilo :p", 0.1)




