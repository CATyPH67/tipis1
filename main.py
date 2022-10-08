import signal_plot

if __name__ == '__main__':
    for i in range(4):
        x, y = signal_plot.create_harmonic(1, 300, 2**i)
        signal_plot.show(x, y)

    for i in range(4):
        x, y = signal_plot.create_digital(1, 300, 2**i)
        signal_plot.show(x, y)


