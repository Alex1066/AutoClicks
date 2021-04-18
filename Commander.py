import os


class Commander:

    def __init__(self, click_positions, going_time, returning_time):
        # List of tuples representing the screen positions where the click should occur.
        self.click_positions = click_positions
        # Number of the seconds until the commander reaches destination.
        self.going_time = going_time
        # The returning time for that commander.
        self.returning_time = returning_time

    def cast_to_file(self, clicks=''):
        number = len([file for file in os.listdir("Commanders")]) + 1
        name = "\\commander" + str(number) + ".txt"
        f = open("Commanders" + name, "a")
        for click_position in self.click_positions:
            clicks += str(click_position[0]) + ',' + str(click_position[1]) + ' '
        f.write(clicks)
        f.write("\n%s" % str(self.going_time))
        f.write("\n%s" % str(self.returning_time))
        f.close()
